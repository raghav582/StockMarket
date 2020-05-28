from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.options import Options
import os

# function to take care of downloading file
def enable_download_headless(browser,download_dir):
    browser.command_executor._commands["send_command"] = ("POST", '/session/$sessionId/chromium/send_command')
    params = {'cmd':'Page.setDownloadBehavior', 'params': {'behavior': 'allow', 'downloadPath': "/home/raghav/Desktop/StockMarket/datasets/"}}
    browser.execute("send_command", params)

# instantiate a chrome options object so you can set the size and headless preference
# some of these chrome options might be uncessary but I just used a boilerplate
# change the <path_to_download_default_directory> to whatever your default download folder is located
options = Options()
# options.add_argument("--headless")
options.add_argument("--window-size=1920x1080")
options.add_argument("--disable-notifications")
options.add_argument('--no-sandbox')
options.add_argument('--verbose')
options.add_experimental_option("prefs", {
        "download.default_directory": "/home/raghav/Desktop/StockMarket/datasets/",
        "download.prompt_for_download": False,
        "download.directory_upgrade": True,
        "safebrowsing_for_trusted_sources_enabled": False,
        "safebrowsing.enabled": False
})
options.add_argument('--disable-gpu')
options.add_argument('--disable-software-rasterizer')

# initialize driver object and change the <path_to_chrome_driver> depending on your directory where your chromedriver should be
driver = webdriver.Chrome("chromedriver_linux64/chromedriver", options=options)

# change the <path_to_place_downloaded_file> to your directory where you would like to place the downloaded file
download_dir = "/home/raghav/Desktop/StockMarket/datasets/"

# function to handle setting up headless download
enable_download_headless(driver, download_dir)

# get request to target the site selenium is active on
driver.delete_all_cookies()
driver.get("https://www.bseindia.com/eqstreamer/StreamerMarketwatch.html?flag=1")

# initialize an object to the location on the html page and click on it to download
search_input = driver.find_element_by_xpath('//*[@id="btndwnload"]')
search_input.click()

