# -*- coding: utf-8 -*-
"""
Created on Sun Apr 5 04:53:01 2020

@author: Infraestructura 3D
"""

"""
Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
"""



# =============================================================================
# %% PATHS
# =============================================================================

PATH_chrome = r'D:/LifeWare Technologies/Alarm System/DataCapture/Templates/chromedriver.exe'

# =============================================================================
# %% URLs
# =============================================================================

#An example of how to input the keywords.
#urls = ['https://www.usatoday.com/search/?q=toilet+paper',
#    'https://www.wsj.com/search/term.html?KEYWORDS=toilet%20paper&min-date=2016/04/05&max-date=2020/04/05&isAdvanced=true&daysback=4y&andor=AND&sort=date-desc&source=wsjarticle,wsjblogs,wsjvideo,interactivemedia,sitesearch,wsjpro',
#    'https://www.nytimes.com/search?dropmab=true&endDate=20200405&query=toilet%20paper&sort=newest&startDate=20190405',

#     https://nypost.com/search/toilet+paper/?sf=20180101&orderby=date&order=desc''
#    'https://www.latimes.com/search?s=1&q=toilet+paper',
#    'https://www.washingtonpost.com/newssearch/?datefilter=All%20Since%202005&sort=Date&query=toilet%20paper',

#    'https://www.startribune.com/search/?sort=date-desc&q=toilet+paper',
#    'https://www.newsday.com/search#filter=stories&query=toilet%20paper',
#    "https://www.chicagotribune.com/search/covid+19/100-y/ALL/date/100/",

#    'https://www3.bostonglobe.com/queryResult/search?q=toilet%20paper&p1=BGMenu_Search&arc404=true']

#urls = ['https://www.usatoday.com/search/?q=',
#        ['https://www.wsj.com/search/term.html?min-date=2018/01/01', '&max-date=2020/04/05', '&isAdvanced=true&daysback=4y&andor=AND&sort=date-desc&source=wsjarticle,wsjblogs,wsjvideo,interactivemedia,sitesearch,wsjpro&KEYWORDS='],
#        'https://www.nytimes.com/search?dropmab=true&endDate=20200405&startDate=20180101&sort=newest&query=toilet%20paper',

#        ['https://nypost.com/search/', '', '/?sf=20180101&orderby=date&order=desc', ],
#        'https://www.latimes.com/search?s=1&q=',
#        'https://www.washingtonpost.com/newssearch/?datefilter=All%20Since%202005&sort=Date&query=',

#        'https://www.startribune.com/search/?sort=date-desc&q=',
#        'https://www.newsday.com/search#filter=stories&query=',
#        "https://www.chicagotribune.com/search/covid+19/100-y/ALL/date/100/",

#        ['https://www3.bostonglobe.com/queryResult/search?','q=toilet%20paper','&p1=BGMenu_Search&arc404=true']
#        ]



urls = {'usa_today': ['https://www.usatoday.com/search/?q=','&page='],
'wsj': ['https://www.wsj.com/search/term.html?min-date=2018/01/01&max-date=','&page=', '&isAdvanced=true&andor=AND&sort=date-desc&source=wsjarticle,wsjblogs,wsjvideo,interactivemedia,sitesearch,wsjpro&KEYWORDS='],
'ny_t': ['https://www.nytimes.com/search?dropmab=true&endDate=','&startDate=20180101&sort=newest&query='],

'ny_p': ['https://nypost.com/search/', '/?sf=20180101&orderby=date&order=desc'],
'la_t': ['https://www.latimes.com/search?s=','&q='],
'washington_p': ['https://www.washingtonpost.com/newssearch/?datefilter=All%20Since%202005&sort=Date&query='],

'star_t': ['https://www.startribune.com/search/?sort=date-desc&q='],
'news_day': ['https://www.newsday.com/search#filter=stories&query='],
'chicago_t': ['https://www.chicagotribune.com/search/','/100-y/ALL/date/100/'],
'boston_g': ['https://www3.bostonglobe.com/queryResult/search?q=','&p', '=BGMenu_Search&arc404=true']
}


# masks format ['separator for words', 'format of date', 'Does it have different pages?', [array. index of the string number where the search, the date, and the pagination must be joined]]
masks = {'usa_today': {'q_sep':['+', 0], 'pag':[True,1]},
         'wsj': {'q_sep': ['%20', 2], 'd_sep': ['/',0], 'pag':[True,1]},
         'ny_t': {'q_sep':['%20',1], 'd_sep':['',0]},

         'ny_p': {'q_sep':['%20',0]},
         'la_t': {'q_sep':['+',1], 'pag':[True,0]},
         'washington_p': {'q_sep':['%20',0]},

         'star_t': {'q_sep': ['+',0]},
         'news_day': {'q_sep':['%20',0]},
         'chicago_t': {'q_sep':['+',0]},

         'boston_g': {'q_sep':['%20',0], 'pag':[True,1]}
        }


#html_tags = {'usa_today': {'general_class':['class', 'gnt_se_a'], 'news_link':['href','gnt_se_a'], 'news_tag':'dat-c-ssts', 'description':'data-c-desc', 'photo_video_link':'gnt_se_f_i','date':'data-c-dt','author':'data-c-by','pag':'gnt_se_pgn_pg'},
#         'wsj': {'general_class':['class', 'item-container headline-item'], 'news_link':['class','gnt_se_a'], 'news_tag':'dat-c-ssts', 'description':'data-c-desc', 'photo_video_link':'gnt_se_f_i','date':'data-c-dt','author':'data-c-by','pag':'gnt_se_pgn_pg'},
#         'ny_t': {'q_sep':['%20',1], 'd_sep':['',0]},
#
#         'ny_p': {'q_sep':['%20',0]},
#         'la_t': {'q_sep':['+',1], 'pag':[True,0]},
#         'washington_p': {'q_sep':['%20',0]},
#
#         'star_t': {'q_sep': ['+',0]},
#         'news_day': {'q_sep':['%20',0]},
#         'chicago_t': {'q_sep':['+',0]},
#
#         'boston_g': {'q_sep':['%20',0], 'pag':[True,1]}
#        }


#html_tags = {'usa_today': {'general_class':['class', 'gnt_se_a']},
#         'wsj': {'general_class':['class', 'item-container headline-item']},
#         'ny_t': {'q_sep':['%20',1], 'd_sep':['',0]},
#
#         'ny_p': {'q_sep':['%20',0]},
#         'la_t': {'q_sep':['+',1], 'pag':[True,0]},
#         'washington_p': {'q_sep':['%20',0]},
#
#         'star_t': {'q_sep': ['+',0]},
#         'news_day': {'q_sep':['%20',0]},
#         'chicago_t': {'q_sep':['+',0]},
#
#         'boston_g': {'q_sep':['%20',0], 'pag':[True,1]}
#        }

# =============================================================================
# %% Imports
# =============================================================================

import numpy as np
import pandas as pd
from threading import Thread
from threading import Timer
import gc,requests,json
from datetime import datetime
from bs4 import BeautifulSoup

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

import time


# =============================================================================
# %% Functions
# =============================================================================

def downloadPage(url,verbose):

    page = requests.get(url)
    print('Status Code: '+str(page.status_code))
    if verbose:
        print(page)

    return page





# =============================================================================
# %% Settings
# =============================================================================

keyword = 'toilet paper'
end_date = str(datetime(2020, 4, 5))[:10]


# =============================================================================
# %% Download Pages
# =============================================================================

browser = webdriver.Chrome(executable_path=PATH_chrome)
pages_ = {}

# iter through the urls and its masks
keys = list(urls.keys())
for key in keys:
    url = urls[key]
    mask = masks[key]
    
    keys_mask = list(mask.keys())
    
    n = False
    
    for key_mask in keys_mask:
        if key_mask == 'q_sep':
            #convert the work into a readable format for the databse of the page
            keyword_temp = keyword.replace(' ', mask[key_mask][0])
            idx = mask[key_mask][1]
            url[idx] = ''.join([url[idx],keyword_temp])
            
        elif key_mask == 'd_sep':
            end_date_temp = end_date.replace('-', mask[key_mask][0])
            idx = mask[key_mask][1]
            url[idx] = ''.join([url[idx],end_date_temp])
            
        elif key_mask == 'pag':
            n = 1
            #TO DO: ge the number of pages so is easier to iterate through.
            idx = mask[key_mask][1]
            url_pag = url.copy()
            url[idx] = ''.join([url[idx],str(n)])

    pages_[key] = {}
    
    if url:
        
        url = ''.join(url)
        
        print(url)
        
        browser.get(url)
        time.sleep(2)
        content = browser.page_source
        
        page_parsed = BeautifulSoup(content, 'html.parser')
        wait = WebDriverWait(browser, 600)
        
        #Get the individual News
        news = page_parsed.find_all(class_= html_tags[key]['general_class'][1])
        
        pages_[key]['page_'+str(n)] = news
        
        #get the pagination numbers
        pag = page_parsed.find_all(class_= html_tags[key]['pag'])
        pag = len(pag)
        
        for n in range(2,pag+1):
            #TO DO: ge the number of pages so is easier to iterate through.
            idx = mask[key_mask][1]
            url = url_pag.copy()
            url[idx] = ''.join([url_pag[idx],str(n)])
            
            url = ''.join(url)
            
            print(url)
            
            browser.get(url)
            time.sleep(2)
            content = browser.page_source
            
            page_parsed = BeautifulSoup(content, 'html.parser')
            wait = WebDriverWait(browser, 600)
            
            
            f = open(key+'.txt', 'wb')
            f.write(content.encode())
            f.close()
            

            
            
            # Iter through every news link
    #        for item in news:
    #            
    #            
    #        
    #        #Get the values and links
    #        news = page_parsed.find_all(class_= html_tags[key]['news_link'])
    #        html_keys = list(html_tags[key].keys())
    #
    #        pages_[key] = content
    #        
    #        
    #        f = open(key+'.txt', 'wb')
    #        f.write(content.encode())
    #        f.close()





# =============================================================================
# %% End
# =============================================================================



