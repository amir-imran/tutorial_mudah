import os
import time

import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By

os.environ['PATH'] += r"C:\SeleniumDriver\chromedriver.exe"
driver = webdriver.Chrome()

driver.get('https://www.mudah.my/')

driver.find_element(By.XPATH, '//*[@id="__next"]/div[2]/div/div[1]/div[1]/div/div/div[2]/div[2]/a').click()

time.sleep(7)
driver.find_element(By.XPATH, '//button[contains(@class, "mw163 mw134 mw142 mw744")]').click()

time.sleep(1)
driver.find_element(By.CSS_SELECTOR, '#__next > div.mw11.mw12 > div > div.mw11.mw25 > div.mw26.mw27.mw49 > div.mw26.mw28.mw70 > div:nth-child(1) > div:nth-child(1) > div > button').click()

time.sleep(1)
driver.find_element(By.CSS_SELECTOR, '#__next > div.mw11.mw12 > div > div.mw11.mw25 > div.mw26.mw27.mw49 > div.mw26.mw28.mw70 > div:nth-child(1) > div:nth-child(1) > div > div > ul > li:nth-child(1)').click()

driver.find_element(By.ID, "brand-and-model-autocomplete").send_keys("SONY PS5")
driver.find_element(By.XPATH, '//*[@id="__next"]/div[2]/div/div[2]/div[1]/div[2]/button[1]').click()

time.sleep(2)
titles = driver.find_elements(By.XPATH, '//a[@class="sc-cJSrbW ciMzjx"]')
prices = driver.find_elements(By.XPATH, '//div[@class="sc-frDJqD dXihyo"]')

data = []
temporarydata={}

for i in range(len(titles)):
    temporarydata= {'Product': titles[i].text, 'Price': prices[i].text}
    data.append(temporarydata)

print(data)

df = pd.DataFrame(data)
print(df)
