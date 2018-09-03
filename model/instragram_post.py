# -*- coding: utf-8 -*-
"""
Created on Fri Aug 10 11:21:04 2018

@author: anjalidharmik
"""

import selenium
import time
from selenium import webdriver
from bs4 import BeautifulSoup
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
import re,json
import pandas as pd
import os
from pandas.io.json import json_normalize
import time,sys

def collect_post_from_the_website(url,output_fldr):
    #using google chrome...
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument("user-agent=ua.chrome()")
    browser = webdriver.Chrome(chrome_options=chrome_options,executable_path="/usr/lib/chromium-browser/chromedriver")
    browser.get(url)
    #print(browser.title)
   
    #scrolling down...
    pause = 3
    
    lastHeight = browser.execute_script("return document.body.scrollHeight")
    #print(lastHeight)
    
    count = 1
    sub_url_lst =[]
    i = 0
    browser.get_screenshot_as_file("test03_1_"+str(i)+".jpg")
    while True:
        browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(pause)
        newHeight = browser.execute_script("return document.body.scrollHeight")
        #print(newHeight)
        if newHeight == lastHeight:
            break
        lastHeight = newHeight
        i += 1
    
        #extract JSON from web pages...
        source = BeautifulSoup(browser.page_source)
    
        #extract post from web pages...
        for a in source.find_all('a', href=True):
            if "http" not in a['href']:
                sub_url = "https://www.instagram.com"+ a['href']
                if "https://www.instagram.com/p/" in sub_url:
                    #print(str(count),sub_url)
                    sub_url_lst.append([sub_url])
                    count +=1
    browser.quit()
    df = pd.DataFrame(sub_url_lst,columns=['post'])
    df.drop_duplicates(['post'],keep='first')
    
    
    
    df.to_csv(output_fldr+"Instagram_data_post.csv",index=False)
#    return df
                 
#output_fldr = "/home/anjalidharmik/Instagram/output2/"
#url = "https://www.instagram.com/anjali"
#collect_post_from_the_website(output_fldr,url)
