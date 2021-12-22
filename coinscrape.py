import requests
from bs4 import BeautifulSoup
import re

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

import pandas as pd

df = pd.read_csv("/Users/avisihag/Desktop/Crypto/filea.csv")

df1 = df.groupby(["category"]).head(2).reset_index(drop=True)

grouped_df = df.groupby('category')


driver = webdriver.Firefox()

for i in df['name']:
    driver.get("https://www.coingecko.com/en/")

    time.sleep(8)
    a = driver.find_element_by_tag_name("input")
    time.sleep(2)
    # WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//tag [contains( text(), 'Overall Score:')]"))).click()
    a.send_keys(i)

    d = driver.find_element_by_xpath("//tag [contains( text(), 'Overall Score:')]")
    print(d.text)
    break

# r = requests.get("https://www.coingecko.com/en/coins/aave#security")

# soup_data = BeautifulSoup(r.text, 'html.parser')

# print(soup_data.find_all("div", {'string':re.compile("Overall Score:")}))


