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
        self.browser = None

    def load_browser(self):
        options = webdriver.chrome.options.Options()
        options.add_argument("user-agent = Chrome/33.0.1750.517")
        options.add_argument("--disable-dev-shm-usage")
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-extensions")

        path = 'chromedriver_linux64/chromedriver'
        self.browser = webdriver.Chrome(path, chrome_options=options)
        agent = self.browser.execute_script('return navigator.userAgent')
        print(agent)
        self.browser.get("https://www.nseindia.com")

        # while(waitE.visibility_of_element_located((By.TAG_NAME, 'table'))):
        #     time.sleep(2)

        market_data = self.browser.find_element_by_xpath('//*[@id="main_navbar"]/ul/li[2]/a')
        ActionChains(self.browser).move_to_element(market_data).perform()

        time.sleep(2)
        waitE.visibility_of_element_located((By.LINK_TEXT, 'Equity & SME Market'))
        equity = self.browser.find_element_by_link_text('Equity & SME Market')
        equity.click()

        self.browser_refresh()

        time.sleep(5)
        waitE.visibility_of_element_located((By.XPATH, '//*[@id="equityStockTable"]/tbody/tr[51]'))
        head = self.browser.find_element_by_xpath('//*[@id="equityStockTable"]/thead/tr')
        rows = self.browser.find_elements_by_xpath('//*[@id="equityStockTable"]/tbody/tr')
        self.equity_data = self.equity_data.append(pd.DataFrame(head.text.split(" ")).T)
        time.sleep(2)

        for row in rows:
            self.equity_data = self.equity_data.append(pd.DataFrame(row.text.split(" ")).T)

    def get_data(self):
        return self.equity_data

    def browser_refresh(self):
        time.sleep(2)
        self.browser.delete_all_cookies()
        self.browser.refresh()
