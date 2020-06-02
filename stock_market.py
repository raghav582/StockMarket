"""
Created on 14/05/20

@author: raghav
"""

from browser_automation import Browser_Automation
import pandas as pd
import datetime

BA_obj = Browser_Automation()
BA_obj.load_browser()
today_date = str(datetime.date.today())
data_path = "datasets/MarketWatch_"+today_date.split("-")[2]+"_"+today_date.split("-")[1]+"_"+today_date.split("-")[0]+"_lastupdatedon_04_00 PM.csv"
data = pd.read_csv(data_path)
data.to_csv('datasets/'+today_date+'.csv')