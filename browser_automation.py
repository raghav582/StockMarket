#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri May  8 15:00:07 2020

@author: raghav
"""

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

browser = webdriver.Chrome('chromedriver_linux64/chromedriver')

browser.get("https://www.bseindia.com/eqstreamer/StreamerMarketwatch.html?flag=1")

# locator
link = browser.find_element_by_xpath('//*[@id="btndwnload"]')
link.click()

download_csv = browser.find_element_by_xpath('//*[@id="ContentPlaceHolder1_imgDownload"]')
download_csv.click()