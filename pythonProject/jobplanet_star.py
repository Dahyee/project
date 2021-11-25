'''
잡플레닛 평점/리뷰개수 크롤링
'''

import requests
from bs4 import BeautifulSoup
import pymysql
import pandas as pd
import selenium
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


# 크롤링
url = "https://www.jobplanet.co.kr/search?query=%EC%95%A0%EB%8B%88%ED%8C%8C%EC%9D%B4%EB%B8%8C"
headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Safari/537.36"}
res = requests.get(url, headers=headers)
res.raise_for_status()

soup = BeautifulSoup(res.text, "lxml")

print("[애니파이브]")

# 별점
stars = soup.find_all("span", attrs={"class":"rate_ty02"})
for star in stars:
    star = star.get_text()
    print("별점 : " + star)

    break

# 세부링크
links = soup.find_all("span", attrs={"class":"llogo"})
for link in links:
    link = "https://www.jobplanet.co.kr/" + link.find("a")["href"]
    print("링크 : " + link)

    break


# --------------------------------------------
# 받아온 링크로 세부 페이지 다시 크롤링
res = requests.get(link, headers=headers)
res.raise_for_status()

soup = BeautifulSoup(res.text, "lxml")

# 리뷰 개수
review_counts = soup.find_all("div", attrs={"class":"result"})
for review_count in review_counts:
    review_count = review_count.find("span", attrs={"class":"num"}).get_text()
    print("리뷰개수 : " + review_count)

reviews = soup.find_all("div", attrs={"class":"content_body_ty1"})
print(reviews)
