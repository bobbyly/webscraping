from selenium import webdriver
from bs4 import BeautifulSoup
import time
import numpy
import os
import datetime
import requests

start_time = time.time()
currentDT = datetime.datetime.now()
http_proxy = "http://bly6:"+input('wordo')+"@httpgw.kmtltd.net.au:8080"
proxyDict = {
              "http"  : http_proxy,
              "https" : http_proxy,
            }

options = webdriver.ChromeOptions()
prefs = {"profile.default_content_setting_values.geolocation": 2}
options.add_experimental_option("prefs", prefs)
options.add_argument('--proxy=http://httpgw.core.kmtltd.net.au:8080')
browser = webdriver.Chrome(options=options)
# urllib.request.ProxyHandler(proxies=proxyDict)

newpath = r'G:\Kmart Merch – BAF\Beauty\BAF Competition Web\D001_BEST_LESS'+currentDT.strftime("%Y%m%d")
if not os.path.exists(newpath):
    os.makedirs(newpath)

browser.get('https://www.bestandless.com.au/Shoes-For-The-Family/Womens-Shoes/c/shoes-women?sort=price-desc&q=%3AnewArrival-asc')
# click 'load more' until there is no more to be loaded
while True:
    try:
        load_more = browser.find_element_by_xpath('//*[@id="main-content"]/div[6]/div[1]/div/button/div')
        load_more.click()
    except:
        continue
    else:
        load_more.click()
        break

time.sleep(3)
source = browser.page_source
soup = BeautifulSoup(source, 'html.parser')
addresslist = [('name', 'sku code', 'picture link', 'price')]
for address in soup.find_all('div', {'class': 'col-6 col-md-4 col-lg-3 cat-item'}):
    link = address.find('img')['src']
    price = address.find('div', {'class': 'cat-item-price'})
    name = address.find('h4', {'class': 'cat-item-name text-capitalize text-muted'})
    title = name.text.strip('\n')
    sku_url = address.find('a')['href'].split('/p/')[1]
    list_price = price.text.strip('\n').strip('from').replace('\n', ' was ')
    # addresslist.append(title)
    # addresslist.append(sku_url)
    # addresslist.append(link)
    # addresslist.append(price.text.strip('\n').strip('from').replace('\n', ' was '))
    addresslist.append((title, sku_url, link, list_price))
    r = requests.get(link, proxies=proxyDict, verify=False)
    with open(newpath + '\\' + title + ' ' + sku_url + ".jpg", 'wb') as f:
        f.write(r.content)


numpy.savetxt(newpath+'\\'+'D001BESTLESS'+currentDT.strftime("%Y%m%d")+'.csv', addresslist, fmt="%s", delimiter=',')
browser.close()
print("seconds taken: ", time.time() - start_time)
