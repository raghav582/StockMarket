#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri May  8 15:00:07 2020

@author: raghav
"""

from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
import time

browser = webdriver.Chrome('chromedriver_linux64/chromedriver')
browser.get("https://www.nseindia.com/market-data/live-equity-market")
time.sleep(20)
download_csv = browser.find_element_by_link_text("Download (.csv)")
ActionChains(browser).move_to_element(download_csv).click(download_csv).perform()
# browser.execute_script('javascript:dnldEquityStock()')