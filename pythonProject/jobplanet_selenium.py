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

# driver.find_element_by_xpath("//*[@id=\"mainContents\"]/div[1]/div/div[2]/div[1]/div[1]/a").click()     # full xPath

summary = []
pros = []
cons = []
comment = []

'''
for i in range(0,5):
    driver.find_element_by_xpath("/html/body/div[1]/div[3]/div/div[1]/div[3]/article[2]/div/div/div/div[6]/article/a["+str(i+2)+"]").click()     # full xPath

    soup = BeautifulSoup(driver.page_source, 'html.parser')

    summary.append(soup.select('h2.us_label')[i].text.split('"')[1])
    pros.append(soup.select('dl.tc_list')[i].select('dd.df1')[0].text)
    cons.append(soup.select('dl.tc_list')[i].select('dd.df1')[1].text)
    comment.append(soup.select('dl.tc_list')[i].select('dd.df1')[2].text)

    print(summary)
    print(pros)
    print(cons)
    print(comment)



res = pd.DataFrame({'요약': summary,
                   '장점': pros,
                   '단점': cons,
                   '코멘트': comment})
res = res.replace(r'\n','',regex = True)
res.to_excel('jobplanet_review_crawling.xlsx')
res.head()
print('작업이 완료되었습니다.')


time.sleep(2)
'''

# 팝업창 닫기
main = driver.window_handles 
for handle in main: 
    if handle != main[0]: 
        driver.switch_to_window(handle) 
        driver.close()

'''
for button in buttons:
    button.click()
    print(button)
'''

# 리뷰 크롤링
reviews = driver.find_elements_by_class_name("us_label")
for review in reviews:
    review = reviews
    print(review)



