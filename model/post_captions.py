# -*- coding: utf-8 -*-
"""
Created on Thu Aug  9 17:55:08 2018

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

def profile_cap(url,username,slot_value,output_fldr_path):
    all_medias =[]

    
    #browser = webdriver.PhantomJS("phantomjs")
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument("user-agent=ua.chrome()")
    driver = webdriver.Chrome(chrome_options=chrome_options,executable_path="/usr/lib/chromium-browser/chromedriver")
    driver.get(url)
    #print(browser.title)
    
    soup = BeautifulSoup(driver.page_source)
    try:
        script_tag = soup.find('script',text = re.compile('window\._sharedData'))
        shared_data = script_tag.string.partition('=')[-1].strip(' ;')
        
        result = json.loads(shared_data)
        
        post_text = result['entry_data']['PostPage'][0]['graphql']['shortcode_media']['edge_media_to_caption']['edges'][0]['node']['text']
        _timestamp = result['entry_data']['PostPage'][0]['graphql']['shortcode_media']['taken_at_timestamp']
        num_comments = result['entry_data']['PostPage'][0]['graphql']['shortcode_media']['edge_media_to_comment']['count']
        
        user_id = result['entry_data']['PostPage'][0]['graphql']['shortcode_media']['id']
        owner_id = result['entry_data']['PostPage'][0]['graphql']['shortcode_media']['owner']['id']
        
        date_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(int(_timestamp)))
        
        for d in range(0,len(result['entry_data']['PostPage'])):
            user_id = result['entry_data']['PostPage'][int(d)]['graphql']['shortcode_media']['display_url']
            all_medias.append(user_id)
        
        short_json_list = {"Media":all_medias,"Post":post_text,"Comments":num_comments,"PostedOn":date_time,"MediaID":str(user_id)+"__"+str(owner_id),\
                            "PostUrl":url,"Username": username}
        
        driver.quit()
        
        return short_json_list
    except:
        pass
        driver.quit()
