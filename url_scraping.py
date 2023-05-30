from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pandas as pd
import time
import re
options = webdriver.ChromeOptions()
options.add_experimental_option("excludeSwitches", ["enable-logging"])
driver = webdriver.Chrome(
    options=options, executable_path=r'./chromedriver.exe')
driver.maximize_window()
members_list = []
URL_list = []
for i in range(1, 10):
    driver.get(f"https://www.am-switzerland.ch/en/ueber-uns/mitglieder/mitgliederverzeichnis/p{i}")
    cards = driver.find_elements(By.XPATH, '/html/body/main/div/div/div[2]/div/div/div[2]/div/div/div')
    for card in cards:
        members = card.find_element(By.TAG_NAME, 'h3').text
        members_list.append(members)
        print(members)
        tables = card.find_elements(By.TAG_NAME, 'a')
        # for table in tables:
        #     a = table.get_attribute("href")
        #     print(a)
        try:
            url= tables[1].get_attribute("href")
        except:
            url = "not_found"
        print(url)
        URL_list.append(url)
        dict = {'member': members_list, 'URL': URL_list}

        df = pd.DataFrame(dict)

        df.to_csv('Result.csv')

