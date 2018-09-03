# -*- coding: utf-8 -*-
"""
Created on Thu Aug  9 11:01:13 2018

@author: anjalidharmik
"""

import instragram_post,post_captions
import pandas as pd
import time,sys

if __name__ == "__main__":
    start = time.time()
    url = sys.argv[1]
    output_fldr = sys.argv[2]

    instragram_post.collect_post_from_the_website(output_fldr,url)

    df_in = pd.read_csv(output_fldr+"Instagram_data_post.csv")
    post_captions.post_caption(output_fldr,df_in)

    print("Takes time: " + str(time.time() - start) +" seconds")
    
    
