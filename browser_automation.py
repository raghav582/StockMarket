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
import pandas as pd


class Browser_Automation:
    def __init__(self):
        self.equity_data = pd.DataFrame()

    def load_browser(self):
        user_agent = 'Chrome/33.0.1750.517'
        options = webdriver.chrome.options.Options()
        options.add_argument(f'user-agent={user_agent}')

        browser = webdriver.Chrome('chromedriver_linux64/chromedriver', chrome_options=options)
        browser.get("https://www.nseindia.com/")

        # while(waitE.visibility_of_element_located((By.TAG_NAME, 'table'))):
        #     time.sleep(2)

        market_data = browser.find_element_by_xpath('//*[@id="main_navbar"]/ul/li[2]/a')
        ActionChains(browser).move_to_element(market_data).perform()

        time.sleep(2)
        equity = browser.find_element_by_link_text('Equity & SME Market')
        equity.click()

        time.sleep(2)
        head = browser.find_element_by_xpath('//*[@id="equityStockTable"]/thead/tr')
        rows = browser.find_elements_by_xpath('//*[@id="equityStockTable"]/tbody/tr')
        self.equity_data = self.equity_data.append(pd.DataFrame(head.text.split(" ")).T)
        time.sleep(2)

        for row in rows:
            self.equity_data = self.equity_data.append(pd.DataFrame(row.text.split(" ")).T)

    def get_data(self):
        return self.equity_data
