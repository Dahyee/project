'''
네이버 웹툰 크롤링하기 2
'''

import requests
from bs4 import BeautifulSoup

url = "https://comic.naver.com/webtoon/weekday"
res = requests.get(url)
res.raise_for_status()                   # 오류 발생 시 프로그램 종료

# 받아온 text를 lxml 을 통해 bs 객체로 만들기
soup = BeautifulSoup(res.text, "lxml")


# 요일별 전체 웹툰 가져오기
print("[요일별 전체 웹툰 가져오기]")
cartoons = soup.find_all("a", attrs={"class":"title"})  # list 로 변환
for cartoon in cartoons:
    print(cartoon.get_text())
print()


# 특정 웹툰(독립 일기) 정보 가져오기
url = "https://comic.naver.com/webtoon/list?titleId=748105"
res = requests.get(url)
res.raise_for_status()               # 오류 발생 시 프로그램 종료

soup = BeautifulSoup(res.text, "lxml")


# 제일 최신 웹툰 회차 제목과 링크 정보 가져오기
cartoons = soup.find_all("td", attrs={"class":"title"})
title = cartoons[0].a.get_text()
link = cartoons[0].a["href"]

print("[제일 최근 회차 제목] : " + title)
print("[제일 최근 회차 링크] : " + link)
print("[제일 최근 회차 링크] : https://comic.naver.com" + link)
print()


# 모든 타이틀의 제목 정보
print("[모든 회차 정보]")
for cartoon in cartoons:
    title = cartoon.a.get_text()
    link = "https://comic.naver.com" + cartoon.a["href"]
    print(title, link)
print()


# 회차별 평점 가져오기
total_rates = 0
cartoons = soup.find_all("div", attrs={"class":"rating_type"})

for cartoon in cartoons:
    rate = cartoon.find("strong").get_text()
    total_rates += float(rate) 
    
print("[전체 점수] : " + total_rates)
print("[평균 점수] : " + total_rates/len(cartoons))
print()