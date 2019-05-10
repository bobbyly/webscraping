from selenium import webdriver
from bs4 import BeautifulSoup
import time
import numpy
# import urllib.request
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

newpath = r'G:\Kmart Merch – BAF\Beauty\BAF Competition Web\D020_BIG_W'+currentDT.strftime("%Y%m%d")
if not os.path.exists(newpath):
    os.makedirs(newpath)

page_url = [0]
for each in page_url:
    browser.get('https://www.bigw.com.au/beauty-health/makeup-cosmetics/c/6220/?pageSize=144&q=%3Apricenat-desc%3AbrandName%3AAustralis%3AbrandName%3AMaybelline%3AbrandName%3ASinful%2BColors%3AbrandName%3Ae.l.f.&page='+str(each))
    time.sleep(3)
    source = browser.page_source
    soup = BeautifulSoup(source, 'html.parser')
    addresslist = []
    broil = soup.find('div', {'class': 'product-listing'})
    for address in broil.find_all('div', {'class': 'productSlot'}):
        link = 'https://www.bigw.com.au'+str(address.find('img', {'class': 'img-responsive image-replace'})['data-src'])
        price = address.find('span', {'class': 'priceClass'})
        name = str(address.find('a')['title']).replace('/', '').replace('*', '').replace(',', '')
        sku_url = str(address.find('a')['data-product-code']).replace('/', '').replace('*', '').replace(',', '')
        addresslist.append((name, sku_url, link, price.text))
        r = requests.get(link, proxies=proxyDict, verify=False)
        with open(newpath+'\\'+name+' '+sku_url+".jpg", 'wb') as f:
            f.write(r.content)

numpy.savetxt(newpath+'\\'+'D020BIGW'+currentDT.strftime("%Y%m%d")+'.csv', addresslist, fmt="%s", delimiter=',')
browser.close()
print("seconds taken: ", time.time() - start_time)