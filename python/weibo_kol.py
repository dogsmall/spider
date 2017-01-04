import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
import hashlib
import csv
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class PythonOrgSearch(unittest.TestCase):

    def setUp(self):
        self.chromeOptions = webdriver.ChromeOptions()
        prefs = {"profile.managed_default_content_settings.images": 2}
        self.chromeOptions.add_experimental_option("prefs", prefs)
        self.driver = webdriver.Chrome(chrome_options=self.chromeOptions)

    def test_search_in_python_org(self):
        driver = self.driver

        driver.get("http://weibo.com/login.php")
        # self.assertIn("Python", driver.title)
        driver.delete_all_cookies()
        elem = driver.find_element_by_id("loginname")
        elem.send_keys("18335153609")
        passelem = driver.find_element_by_name("password")
        passelem.send_keys("guoshiwei")
        passelem.send_keys(Keys.RETURN)
        # cookie = driver.get_cookies()
        # driver.find_element_by_name("password")
        # print(cookie)
        # driver.add_cookie(cookie)
        f = open("./weibo_kol.txt")
        items = f.read()
        itemlist = items.split("\n")
        f.close()
        for item in itemlist:
            # print(item.split('\t')[2])
            # row = item.split('\t')[2].replace('#', '')
            # hash_md5 = hashlib.md5(row.encode(encoding='utf-8'))
            # uid = hash_md5.hexdigest()
            url = item.split('\t')[2]
            print(url)
            # driver.implicitly_wait(10)
            driver.get(url)
            time.sleep(5)
            soup = BeautifulSoup(driver.page_source, 'lxml')
            try:
                neirong = soup.find(
                    'div', {"class": "WB_text W_f14"}).text.strip()
                print(neirong)
            except BaseException as identifier:
                neirong = "没有内容"
            try:
                riqi = soup.find('div', class_="WB_from S_txt2").find(
                    'a', class_="S_txt2").text.strip()
            except BaseException as identifier:
                riqi = "没有日期"
            try:
                zhuanfa = soup.find_all('span', class_="pos")[
                    1].find_all("em")[1].text.strip()
            except BaseException as identifier:
                zhuanfa = "没有转发"
            try:
                pinlu = soup.find_all('span', class_="pos")[
                    2].find_all("em")[1].text.strip()
            except BaseException as identifier:
                pinlu = "没有评论"
            try:
                dianzan = soup.find_all('span', class_="pos")[
                    3].find_all("em")[1].text.strip()
            except BaseException as identifier:
                dianzan = "没有点赞"
            res = [url + "\t" + zhuanfa + "\t", pinlu + "\t",
                   dianzan + "\t", neirong + "\t", riqi + "\n", ]
            w = open("index.txt", "a+")
            w.writelines(res)
            w.close()

            # assert "No results found." not in driver.page_source

    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()
