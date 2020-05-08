#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri May  8 15:00:07 2020

@author: raghav
"""

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver=webdriver.Chrome("Desktop/StockMarket/chromedriver_linux64/chromedriver")
driver.get("https://www1.nseindia.com/live_market/dynaContent/live_watch/equities_stock_watch.htm")