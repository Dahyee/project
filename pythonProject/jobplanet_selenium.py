'''
잡플레닛 리뷰 크롤링
'''

import requests
from bs4 import BeautifulSoup
import pymysql
import pandas as pd
import selenium
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import re

options = webdriver.ChromeOptions()
options.add_argument("disable-gpu")   # 가속 사용 x
options.add_argument("lang=ko_KR")    # 가짜 플러그인 탑재
options.add_argument('user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Safari/537.36')  # user-agent 이름 설정


# 크롬 드라이버 실행 
driver = webdriver.Chrome("C:/Users/user/Desktop/projects/chromedriver", chrome_options=options)
driver.implicitly_wait(3)

driver.get("https://www.jobplanet.co.kr/users/sign_in?_nav=gb")
time.sleep(2)       # 페이지 로딩으로 인한 시간 지연


# 로그인
driver.find_element_by_name('user[email]').send_keys('whyhow9701@hufs.ac.kr')
driver.find_element_by_name('user[password]').send_keys('970130da@@')   
driver.find_element_by_xpath("/html/body/div[1]/div[4]/div/div/div/form/div/div[2]/div/section[2]/fieldset/button").click()     # full xPath
time.sleep(2)


# 검색 input태그 
driver.find_element_by_id('search_bar_search_query').send_keys('애니파이브')
driver.find_element_by_id("search_bar_search_query").send_keys(Keys.ENTER)
time.sleep(2)


# 상세페이지 클릭
bs = BeautifulSoup(driver.page_source, 'html.parser')     # 크롬드라이버 현재 페이지 html 파악
url = re.sub('(?:info)','reviews','https://www.jobplanet.co.kr/'+bs.find("span", attrs={"class":"llogo"}).find("a")["href"])
driver.get(url)


# 팝업창 닫기
driver.find_element_by_class_name("btn_close_x_ty1").click()
time.sleep(2)


# 리뷰 크롤링
summarys = []
advans = []
disadvans = []
comments = []
stars = []

soup = BeautifulSoup(driver.page_source, 'html.parser')     # 크롬드라이버 현재 페이지 html 파악
reviews = soup.find_all("div", attrs={"class":"content_wrap"})

advantage = []  # 장점, 단점
i = 0
for review in reviews:
    # 리뷰
    summary = review.find("h2").get_text()
    summary = summary.replace("BEST", "")
    summary = summary.lstrip()
    summary = summary.rstrip()
    print("리뷰 : " + summary)

    # 장단점
    texts = review.find_all("dd", attrs={"class":"df1"})
    
    i += 1





