import requests
import json
import os
import datetime
import time
import numpy
from bs4 import BeautifulSoup

start_time = time.time()
currentDT = datetime.datetime.now()

#http_proxy = "http://bly6:"+input('input: ')+"@httpgw.kmtltd.net.au:8080"
http_proxy = "httpgw.kmtltd.net.au:8080"
proxyDict = {
              "http": http_proxy,
              "https": http_proxy,
            }
display_count = 48
newpath = r'G:\Kmart Merch – BAF\Beauty\BAF Competition Web\Skincare_BIG_W'+currentDT.strftime("%Y%m%d")
if not os.path.exists(newpath):
    os.makedirs(newpath)
addresslist = [('name', 'sku code', 'price', 'category')]
url = 'https://www.bigw.com.au/beauty-health/skincare/c/6218/?q=%3Arelevance&pageSize='+str(display_count)+'&page='
response = requests.get(url, proxies=proxyDict, verify=False)
count_products = int(response.text.split('totalResults pull-right">')[1].split('Products found</small>')[0].strip())
page_url = [4, 5]

if count_products >= display_count:
    page_url = list(range(0, int(numpy.ceil(count_products/display_count))))

for each in page_url:
    response = requests.get(url+str(each), proxies=proxyDict, verify=False)
    print(response.url)
    products = response.text.split("products_storage= ")[1].split(";")[0]
    products_json = json.loads(products)
    soup = BeautifulSoup(response.text, 'html.parser')
    for slickSlot in soup.find_all('div', {'class': 'slickSlot'}):
        slickSlot.decompose()
    broil = soup.find('div', {'class': 'product-listing'})

    for json_data in products_json:
        name = json_data['name'].replace('/', ' ').replace('*', '')
        sku_code = json_data['id']
        price = json_data['price']
        category = json_data['category']
        addresslist.append((name, sku_code, price, category))
'''
    for address in broil.find_all('div', {'class': 'productSlot'}):
        link = 'https://www.bigw.com.au' + str(address.find('div', {'class': 'delayed-image-load'})['data-src'])
        img_name = str(address.find('a')['title']).replace('/', ' ').replace('*', '')
        img_sku = str(address.find('a')['data-product-code']).replace('/', '').replace('*', '')
        pictures = requests.get(link, proxies=proxyDict, verify=False)
        time.sleep(0.1)
        with open(newpath+'\\'+img_name+' '+img_sku+".jpg", 'wb') as f:
             f.write(pictures.content)
'''
numpy.savetxt(newpath+'\\'+'_Skincare_BIGW'+currentDT.strftime("%Y%m%d")+'.csv', addresslist, fmt="%s", delimiter=',')

print("seconds taken: ", time.time() - start_time)

