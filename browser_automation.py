#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri May  8 15:00:07 2020

@author: raghav
"""
from kombu.utils.eventio import _select
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as waitE
from selenium.webdriver.support.ui import Select
import time
import pandas as pd


class Browser_Automation:
    def __init__(self):
        self.equity_data = pd.DataFrame()
        self.browser = None
        self.datapath = None

    def load_browser(self):
        options = webdriver.chrome.options.Options()
        options.add_argument("user-agent = Chrome/33.0.1750.517")
        options.add_argument("--disable-dev-shm-usage")
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-extensions")
        options.add_experimental_option("prefs",{
            "download.default_directory": "/home/raghav/Desktop/StockMarket/datasets/",
            "download.prompt_for_download": False,
            "download.directory_upgrade": True,
            "safebrowsing_for_trusted_sources_enabled": False,
            "safebrowsing.enabled": False
        })

        path = 'chromedriver_linux64/chromedriver'
        self.browser = webdriver.Chrome(path, chrome_options=options)
        agent = self.browser.execute_script('return navigator.userAgent')
        print(agent)

        self.browser.command_executor._commands["send_command"] = ("POST", '/session/$sessionId/chromium/send_command')
        params = {'cmd': 'Page.setDownloadBehavior',
                  'params': {'behavior': 'allow', 'downloadPath': "/home/raghav/Desktop/StockMarket/datasets/"}}
        command_result = self.browser.execute("send_command", params)

        print(str(command_result))

        self.browser.get("https://www.bseindia.com/markets/Equity/EQReports/MarketwatchDownloads.aspx")
        self.browser_refresh()
        # while(waitE.visibility_of_element_located((By.TAG_NAME, 'table'))):
        #     time.sleep(2)
        index = self.browser.find_element_by_id("ContentPlaceHolder1_ddlType")
        select_source = Select(index)
        select_source.select_by_value("Index")

        sandp = self.browser.find_element_by_id("ContentPlaceHolder1_ddlIndx")
        select_source = Select(sandp)
        select_source.select_by_value("98")

        download = self.browser.find_element_by_id("ContentPlaceHolder1_imgDownload")
        download.click()


    def browser_refresh(self):
        time.sleep(2)
        self.browser.delete_all_cookies()
        self.browser.refresh()

    def getDatapath(self):
        return self.datapath
