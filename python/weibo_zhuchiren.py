import csv
import hashlib
from selenium import webdriver
from bs4 import BeautifulSoup
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

cap = webdriver.DesiredCapabilities.PHANTOMJS

# cap["phantomjs.page.settings.resourceTimeout"] = 1000
cap["phantomjs.page.settings.loadImages"] = False
cap["phantomjs.page.settings.disk-cache"] = True
cap["phantomjs.page.customHeaders.Cookie"] = 'SINAGLOBAL=3251250314579.1147.1470725256414; _s_tentry=www.google.com.hk; Apache=7454531535722.975.1480323060230; ULV=1480323060313:25:10:1:7454531535722.975.1480323060230:1480056594168; YF-V5-G0=35ff6d315d1a536c0891f71721feb16e; login_sid_t=7c6cea2588999f5f0e29f0fb58a70233; YF-Ugrow-G0=1eba44dbebf62c27ae66e16d40e02964; YF-Page-G0=cf25a00b541269674d0feadd72dce35f; WBtopGlobal_register_version=5b56985b93d98642; SSOLoginState=1480323401; wvr=6; SCF=ArqiEfmQWLrAiMojWDMEzkoNs1VLm31c8bsa70mbNqav3ZI3dmsKR3-wt79PJWMaoexKGFr-f7YSm6GQAzXPDIU.; SUB=_2A251P4gnDeTxGeRH6VYZ-C_LyzuIHXVWTP7vrDV8PUJbmtBeLWTXkW9p-8GKKdcFlG1N2q_EchLnN_WvAA..; SUBP=0033WrSXqPxfM725Ws9jqgMF55529P9D9W5f8TiH-ew4DsiVdcFTyJ9K5JpX5o2p5NHD95QE1KzX1hnpS05NWs4Dqcjci--ciK.fi-z7i--fi-2Xi-8Wi--fi-2fiKnNi--4iKn0i-82i--Xi-zRiK.ci--Xi-ihiKLs; SUHB=0U1J2I3J8BI11N; ALF=1511859400; UOR=book.51cto.com,widget.weibo.com,cuiqingcai.com'  # 我删掉了一大部分


driver = webdriver.PhantomJS(desired_capabilities=cap)
# driver.get("www.baidu.com")
for line in open("./zhoulei_topic_1128.txt"):
    print(line.split(',')[0].replace('#', ''))
    row = line.split(',')[0].replace('#', '')
    hash_md5 = hashlib.md5(row.encode(encoding='utf-8'))
    uid = hash_md5.hexdigest()
    url = 'http://weibo.com/p/100808' + uid
    print(url)
    driver = webdriver.PhantomJS(desired_capabilities=cap)
    driver.get(url)
    soup = BeautifulSoup(driver.page_source, 'lxml')
    try:
        zhuchiren = soup.find('div', {"id": "Pl_Core_Ut2UserList__14"}).find(
            'div', {"class": "info_wrap"}).find("a").text
        print(zhuchiren)
        res = [zhuchiren+'\n']
    except BaseException:
        print("Error: 没有主持人")
        # continue
        try:
            shuzi = soup.findAll("strong")
        except BaseException:
            print("Error: 不是话题")
            driver.quit()
            continue
        else:
            print('阅读：' + shuzi[0].text)
            print('讨论:' + shuzi[1].text)
            print('粉丝:' + shuzi[2].text)
            res[0:0]=[row + '\t', shuzi[0].text + '\t', shuzi[1].text +
                "\t", shuzi[2].text + "\n"]
            txt = open('index.txt', "a+")
            txt.writelines(res)
            print(url)
            # driver.close()
            print('end')
            driver.quit()
            # time.sleep(10)
    else:
        try:
            shuzi = soup.findAll("strong")
        except BaseException:
            print("Error: 不是话题")
            driver.quit()
            continue
        else:
            print('阅读：' + shuzi[0].text)
            print('讨论:' + shuzi[1].text)
            print('粉丝:' + shuzi[2].text)
            res[0:0]=[row + '\t', shuzi[0].text + '\t', shuzi[1].text +
                "\t", shuzi[2].text + "\t"]
            txt = open('index.txt', "a+")
            txt.writelines(res)
            print(url)
            # driver.close()
            print('end')
            driver.quit()
            # time.sleep(10)


txt.close()

print('allEnd')
