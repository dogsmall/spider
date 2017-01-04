import csv
import hashlib
from selenium import webdriver
from bs4 import BeautifulSoup
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

url = "http://www.toutiao.com/news_entertainment/"
print(url)
driver = webdriver.Chrome()
driver.get(url)
driver.add_cookie({'expiry': 1796753742, 'httpOnly': False, 'value': 'w:6b896bb711c84cd597532259d26b9d4f',
                   'domain': '.toutiao.com', 'secure': False, 'name': 'uuid', 'path': ' /'})
# console.log(driver.page_source)
soup = BeautifulSoup(driver.page_source, 'lxml')


print('allEnd')
