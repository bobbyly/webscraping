from bs4 import BeautifulSoup
import numpy as np
from selenium import webdriver
import time
start_time = time.time()
options = webdriver.ChromeOptions()
prefs = {"profile.default_content_setting_values.geolocation" :2}
options.add_experimental_option("prefs",prefs)
options.add_argument('--proxy-server=139.162.198.212:3128')
browser = webdriver.Chrome(chrome_options=options)
browser.get('https://www.priceline.com.au/store-locator')
time.sleep(12)

pagesource = browser.page_source
pageno = BeautifulSoup(pagesource, 'html.parser')
pages = pageno.find('div', {'class': 'pages'})
last_page = pages.find('a', {'class': 'last'}).get_text()

addresslist = []
page_dir = []

page_list = np.arange(1, int(last_page)+1)
for each in page_list:
    page_dir.append('https://www.priceline.com.au/store-locator?page='+str(each))

for each in page_dir:
    browser.get(each)
    time.sleep(5)
    soup = BeautifulSoup(browser.page_source, 'html.parser')
    for store in soup.find('div', {'class': 'store-list'}).find_all('address'):
        addresslist.append(store.text)
addresslist = [item.replace('\n', ', ') for item in addresslist]
print(addresslist)
np.savetxt('priceline_LOCATIONS.csv', addresslist, fmt="%s", delimiter=',')
browser.close()
print("seconds taken: ", time.time() - start_time)