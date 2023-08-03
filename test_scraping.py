from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver import ActionChains
from selenium.webdriver.support import expected_conditions as EC
import undetected_chromedriver as uc
import pandas as pd
import time
from webdriver_manager.chrome import ChromeDriverManager
# driver = uc.Chrome(driver_executable_path=ChromeDriverManager(version='114.0.5735.90').install())

# driver.maximize_window()
options = webdriver.ChromeOptions()
options.add_experimental_option("excludeSwitches", ["enable-logging"])
driver = webdriver.Chrome(ChromeDriverManager(version='114.0.5735.90').install())
driver.maximize_window()
driver.get('https://www.yellowpages.com.au/')
time.sleep(10)
elements = driver.find_elements(By.CLASS_NAME, 'icon-container')
for element in elements:
    a = element.text
    print(a)
while True:
    pass