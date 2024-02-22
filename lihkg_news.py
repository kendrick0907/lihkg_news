from bs4 import BeautifulSoup
import pandas as pd
import numpy as np
from urllib.request import urlopen
from selenium.webdriver import Chrome
from selenium.webdriver import ChromeOptions
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from time import sleep

title_ls = []
url_ls = []

chrome_options = ChromeOptions()
prefs = {"profile.default_content_setting_values.notifications" : 2}
chrome_options.add_experimental_option("prefs",prefs)
driver = Chrome(options=chrome_options)

driver.get("https://lihkg.com/category/5?order=hot")

sleep(2)

# loop and find the class of all boxes which include the username, comment, number of likes and dislikes etc.
lihkg_html = BeautifulSoup(driver.page_source,'html.parser')
#result_list = lihkg_html.find_all('div', {'class':'_14BnVEj9rQ5VQKmrIqn9Qj'})
result_list = lihkg_html.find_all('div', {'class': 'vv9keWAXpwoonDah6rSIU _1KV65JcPoDUFZ4o3OEqn4R'})

for result in result_list: 
    title_ls.append(result.find('span',{'_20jopXBFHNQ9FUbcGHLcHH'}).get_text())
    url_ls.append(result.find('a',{'_2A_7bGY9QAXcGu1neEYDJB'})['href'])

# print(url_ls)
