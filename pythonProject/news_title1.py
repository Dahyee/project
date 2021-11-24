'''
한국기업신문 크롤링 
'''

import requests
from bs4 import BeautifulSoup
import pymysql
import pandas as pd

# 디비 연결 객체
news_title_db = pymysql.connect(
    user='root', 
    passwd='doslvkdlqm!', 
    host='192.168.1.116', 
    db='AI_Evaluation', 
    charset='utf8'
)

# DB 와 상호작용하기 위한 cursor 객체 생성
cursor = news_title_db.cursor(pymysql.cursors.DictCursor)


# 예시 - 넥센타이어
url = "http://www.kbenews.com/search.html?submit=submit&search=넥센타이어&imageField3.x=0&imageField3.y=0&search_and=1&search_exec=all&search_section=all&news_order=1&search_start_day=&search_end_day=20211124"
headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Safari/537.36"}
res = requests.get(url, headers=headers)
res.raise_for_status()
soup = BeautifulSoup(res.text, "lxml")

text = soup.find_all("div", attrs={"class":"search_result_list_box"})


print("[넥센타이어 크롤링 예시]")
print()
for title in text:
    news_title = title.find("a").get_text()
    href = "http://www.kbenews.com" + title.find("a")["href"]
    date = title.find("dd", attrs={"class":"etc"}).get_text()

    print(news_title)
    print(href)
    print(date)
    print()
    
   


