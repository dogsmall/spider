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
        f=open("./obj.txt")
        items = f.read()
        itemlist =items.split("\n")
        f.close()
        for item in itemlist:
            print(item.split('\t')[2].replace('#', ''))
            row = item.split('\t')[2].replace('#', '')
            hash_md5 = hashlib.md5(row.encode(encoding='utf-8'))
            uid = hash_md5.hexdigest()
            url = 'http://weibo.com/p/100808' + uid
            print(url)
            driver.implicitly_wait(10)
            driver.get(url)
            time.sleep(5)
            soup = BeautifulSoup(driver.page_source, 'lxml')
            try:

                zhuchiren = soup.find('div', {"id": "Pl_Core_Ut2UserList__14"}).find(
                    'div', {"class": "info_wrap"}).find("a").text
            except BaseException as identifier:

                zhuchiren = "暂无主持人"

            print(zhuchiren)
            try:

                shuzi = soup.findAll("strong")
                yuedu = shuzi[0].text
                taolun = shuzi[1].text
                fensi = shuzi[2].text
                print('阅读：' + shuzi[0].text)
                print('讨论:' + shuzi[1].text)
                print('粉丝:' + shuzi[2].text)
            except BaseException as identifier:
                yuedu = "0"
                taolun = "0"
                fensi = "0"

            res = [row + "\t", yuedu + "\t", taolun +"\t", fensi + "\t", zhuchiren + "\n", ]
            w = open("index.txt","a+")
            w.writelines(res)
            w.close()
            
            
            # assert "No results found." not in driver.page_source

    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()
