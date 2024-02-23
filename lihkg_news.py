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
like_n_dislikes_ls = []
category = input("Please enter the category(News=5, Fin=15): ")

chrome_options = ChromeOptions()
prefs = {"profile.default_content_setting_values.notifications" : 2}
chrome_options.add_experimental_option("prefs",prefs)
driver = Chrome(options=chrome_options)
driver.get("https://lihkg.com/category/{}?order=hot".format(category))

sleep(2)

# loop and find the class of all boxes which include the username, comment, number of likes and dislikes etc.
lihkg_html = BeautifulSoup(driver.page_source,'html.parser')
result_list = lihkg_html.find_all('div', {'class': '_21IQKhlBjN2jlHS_TVgI3l'})

for result in result_list: 
    title_ls.append(result.find('span',{'_20jopXBFHNQ9FUbcGHLcHH'}).get_text())
    url_ls.append(result.find('a',{'_2A_7bGY9QAXcGu1neEYDJB'})['href'])
    like_n_dislikes_ls.append(result.find('div',{'zBQrhafI5njrmUUaJqKA4'}).get_text().split(' ')[-1])

# Walks through the contents of all trending topics. **it's not scraping anything yet
for link in url_ls:
    driver.get("https://lihkg.com{}".format(link))
    sleep(2)
