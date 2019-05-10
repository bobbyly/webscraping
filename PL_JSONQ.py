# -*- coding: utf-8 -*-
"""
Created on Mon Jan  7 09:59:11 2019

@author: bly6
"""
from bs4 import BeautifulSoup
addresslist= []

textdata = open("H:\\Python Scripts\\searchJson.json")

soup = BeautifulSoup(textdata, 'html-parser')
broth = soup.get_text()
for store in soup.find('units'):
    addresslist.append(store.text)
    
    #TypeError: 'NoneType' object is not iterable