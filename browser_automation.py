#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri May  8 15:00:07 2020

@author: raghav
"""

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

browser = webdriver.Chrome("chromedriver_linux64/chromedriver")
browser.get("https://www1.nseindia.com/live_market/dynaContent/live_watch/equities_stock_watch.htm")

browser.maximize_window()

# locator
data = browser.find_element_by_link_text('Download in csv')
data.click()
