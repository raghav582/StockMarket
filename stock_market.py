"""
Created on 14/05/20

@author: raghav
"""

from browser_automation import Browser_Automation

BA_obj = Browser_Automation()
BA_obj.load_browser()
equity_data = BA_obj.get_data()
print(equity_data.head())