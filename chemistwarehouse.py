from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
import time
import numpy

browser = webdriver.Chrome()
browser.get('https://www.chemistwarehouse.com.au/aboutus/store-locator')
search_box = browser.find_element_by_class_name("search-input")

addresslist = []
searchinputs = ['WA']#, 'SA', 'VIC', 'NSW', 'ACT', 'QLD', 'NT']
for states in searchinputs:
    search_box.send_keys(states)
    search_box.send_keys(Keys.ENTER)
    # wait for the js to load the results
    time.sleep(2)
    # capture the new source with the results and parse through bs
    source = browser.page_source
    soup = BeautifulSoup(source, 'html.parser')
    # remove the additional addressed stored in 'gm-style-iw'
    duplicateADD = soup.find('div', {'class': 'gm-style-iw'})
    duplicateADD.decompose()
    # remove the additional information about nursing services
    for nurse in soup.find_all('div', {'style': 'padding:10px;white-space:nowrap;Font-weight:bold;line-height:20px;'}):
        nurse.decompose()
    # find each instance of the 'div class' 'address' and then append to the addresslist
    for address in soup.find_all('div', {'class': 'address'}):
        nextaddresses = address.get_text()
        addresslist.append(nextaddresses)
    search_box.clear()
numpy.savetxt('CHEMISTWAREHOUSE_LOCATIONS.csv', addresslist, fmt="%s", delimiter=',')
browser.close()