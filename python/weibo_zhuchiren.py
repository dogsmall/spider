import csv
import hashlib
from selenium import webdriver
from bs4 import BeautifulSoup
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# cap = webdriver.DesiredCapabilities.PHANTOMJS

# cap["phantomjs.page.settings.resourceTimeout"] = 1000
# cap["phantomjs.page.settings.loadImages"] = False
# cap["phantomjs.page.settings.disk-cache"] = True
# cap["phantomjs.page.settings.userAgent"] = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.98 Safari/537.36"
# cap["phantomjs.page.customHeaders.Cookie"] =
# 'SINAGLOBAL=3251250314579.1147.1470725256414; wvr=6;
# YF-Page-G0=00acf392ca0910c1098d285f7eb74a11;
# SCF=ArqiEfmQWLrAiMojWDMEzkoNs1VLm31c8bsa70mbNqaviYm8dT1Kq5cCrJSXqG5bL4aQoDrTaZoubFcx2zhJwMo.;
# SUB=_2A251T9O-DeRxGeRH6VYZ-C_LyzuIHXVWPUJ2rDV8PUNbmtBeLXPSkW98s7IUgPm4ZfGov6i5tQUoiPLGsg..;
# SUBP=0033WrSXqPxfM725Ws9jqgMF55529P9D9W5f8TiH-ew4DsiVdcFTyJ9K5JpX5KMhUgL.Foz4eoBR1h2NehM2dJLoI0qLxKqL1K-LBo5LxK-LBKBLB-2LxK-LBK-L1hMLxK.L1heLB-BLxKBLBonL1KqLxKBLB.eL1-qt;
# SUHB=0FQrCX2RFk4A0C; ALF=1512888172; SSOLoginState=1481352174;
# _s_tentry=login.sina.com.cn;
# UOR=book.51cto.com,widget.weibo.com,login.sina.com.cn;
# Apache=6492411931057.882.1481352183720;
# ULV=1481352183901:47:7:6:6492411931057.882.1481352183720:1481349339478'
# # 我删掉了一大部分

# driver = webdriver.PhantomJS(desired_capabilities=cap)
# driver.get("www.baidu.com")
for line in open("./zhoulei_topic_1209.txt"):
    print(line.split(',')[2].replace('#', ''))
    row = line.split(',')[2].replace('#', '')
    hash_md5 = hashlib.md5(row.encode(encoding='utf-8'))
    uid = hash_md5.hexdigest()
    url = 'http://weibo.com/p/100808' + uid
    print(url)
    driver = webdriver.Chrome()
    driver.get(url)
    driver.add_cookie({'expiry': 1796753742, 'httpOnly': False, 'value': '2625733745264.132.1481393742727', 'domain': '.weibo.com', 'secure': False, 'name': 'SINAGLOBAL', 'path': ' /'})
    # console.log(driver.page_source)
    soup = BeautifulSoup(driver.page_source, 'lxml')
    try:
        zhuchiren = soup.find('div', {"id": "Pl_Core_Ut2UserList__14"}).find(
            'div', {"class": "info_wrap"}).find("a").text
        print(zhuchiren)
        res = [zhuchiren + '\n']
        print("1")
    except BaseException:
        print("2")
        print("Error: 没有主持人")
        # continue
        try:
            print("4")
            shuzi = soup.findAll("strong")
            print(shuzi)
        except BaseException:
            print("5")
            print("Error: 不是话题")
            driver.quit()
            continue
        else:
            print("6")
            if(len(shuzi) != 0):
                print('阅读：' + shuzi[0].text)
                print('讨论:' + shuzi[1].text)
                print('粉丝:' + shuzi[2].text)
                res = []
                res[0:0] = [row + '\t', shuzi[0].text + '\t', shuzi[1].text +
                            "\t", shuzi[2].text + "\n"]
                txt = open('index.txt', "a+")
                txt.writelines(res)
                txt.close()
                print(url)
                # driver.close()
                print('end')
            else:
                res = []
                res[0:0] = [row + '\t',  '0 \t', "0 \t", "0 \n"]
                txt = open('index.txt', "a+")
                txt.writelines(res)
                txt.close()
                print(url)
                # driver.close()
                print('end')
            driver.quit()

            # time.sleep(10)
    else:
        print("3")
        try:
            print("7")
            shuzi = soup.findAll("strong")
            print(shuzi)
        except BaseException:
            print("8")
            print("Error: 不是话题")
            driver.quit()
            continue
        else:
            print("9")
            if(len(shuzi) != 0):
                print('阅读：' + shuzi[0].text)
                print('讨论:' + shuzi[1].text)
                print('粉丝:' + shuzi[2].text)
                res[0:0] = [row + '\t', shuzi[0].text + '\t', shuzi[1].text +
                            "\t", shuzi[2].text + "\t"]
                txt = open('index.txt', "a+")
                txt.writelines(res)
                txt.close()
                print(url)
                # driver.close()
                print('end')
            else:
                res = []
                res[0:0] = [row + '\t',  '0 \t', "0 \t", "0 \t"]
                txt = open('index.txt', "a+")
                txt.writelines(res)
                txt.close()
                print(url)
                # driver.close()
                print('end')
            driver.quit()
            # time.sleep(10)


print('allEnd')
