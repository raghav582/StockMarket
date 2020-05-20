"""
Created on 14/05/20

@author: raghav
"""

from browser_automation import Browser_Automation
import pandas as pd
import datetime

BA_obj = Browser_Automation()
BA_obj.load_browser()
equity_data = BA_obj.get_data()

while(equity_data.any().isnull().any()):
    BA_obj.browser_refresh()
    equity_data = BA_obj.get_data()

file_path = 'datasets/' + str(datetime.date.today()) + '.csv'
equity_data.to_csv(file_path)
print(equity_data.head())