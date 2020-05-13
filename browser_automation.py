#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri May  8 15:00:07 2020

@author: raghav
"""

from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as waitE
import time

user_agent = 'Chrome/33.0.1750.517'
options = webdriver.chrome.options.Options()
options.add_argument(f'user-agent={user_agent}')


browser = webdriver.Chrome('chromedriver_linux64/chromedriver', chrome_options=options)
browser.get("https://www.bseindia.com/markets.html")

# while(waitE.visibility_of_element_located((By.TAG_NAME, 'table'))):
#     time.sleep(2)

market_data = browser.find_element_by_link_text('Equity')
ActionChains(browser).move_to_element(market_data).click(market_data).perform()

time.sleep(2)
equity = browser.find_element_by_link_text('Equity Market Watch')
equity.click()

time.sleep(2)
rows = browser.find_elements_by_tag_name('tr')
time.sleep(2)
print(len(rows))
