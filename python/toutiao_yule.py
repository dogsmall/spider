import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
import hashlib
import csv
import time
from pymongo import MongoClient
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
client = MongoClient('localhost', 27017)
db = client.test
collection = db.gongzhongs


class PythonOrgSearch(unittest.TestCase):

    def setUp(self):
        self.chromeOptions = webdriver.ChromeOptions()
        prefs = {"profile.managed_default_content_settings.images": 2}
        self.chromeOptions.add_experimental_option("prefs", prefs)
        self.driver = webdriver.Chrome(chrome_options=self.chromeOptions)
        # self.driver.implicitly_wait(30)  # seconds

    def test_search_in_python_org(self):
        driver = self.driver
        driver.get("https://sso.toutiao.com/login/")
        n = 1
        elem = driver.find_element_by_id("mobile")
        elem.send_keys("15116970686")
        passelem = driver.find_element_by_name("code")
        # passelem.send_keys("8881")
        time.sleep(30)
        passelem.send_keys(Keys.RETURN)
        time.sleep(5)
        link = driver.find_element_by_css_selector(("a[href='/news_entertainment/']"));
        link.click()
        time.sleep(5)
        # driver.get("http://www.toutiao.com/news_entertainment/")
        while n < 100:
            try:
                time.sleep(10)
                js = "window.scrollTo(0,document.body.scrollHeight)"
                driver.execute_script(js)
                time.sleep(10)
                n += 1
                print(n)
            except WebDriverException:
                print(u'页面下拉失败')
        soup = BeautifulSoup(driver.page_source, 'lxml')
        source = soup.find_all("a", {"class": "source"})
        for x in source:
            print(x["href"])
            res = [x["href"] + "\n"]
            w = open("toutiao.txt", "a+")
            w.writelines(res)
            w.close()

    def tearDown(self):
        # time.sleep(10)
        self.driver.close()

if __name__ == "__main__":
    unittest.main()
