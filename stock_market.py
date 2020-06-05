"""
Created on 14/05/20

@author: raghav
"""

from browser_automation import Browser_Automation
import pandas as pd
import datetime

BA_obj = Browser_Automation()
BA_obj.load_browser()
# today_date = str(datetime.date.today()).split("-")
# current_time = str(datetime.time).split(":")
# data_path = "datasets/MarketWatch_"+today_date[2]+"_"+today_date[1]+"_"+today_date[0]+"_lastupdatedon_"+current_time[0]+"_"+00 PM.csv"
# data = pd.read_csv(data_path)
# data.to_csv('datasets/'+today_date+'.csv')