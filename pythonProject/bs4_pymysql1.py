'''
네이버 뉴스 >> 속보 
    뉴스 헤드라인 크롤링
'''

import requests
from bs4 import BeautifulSoup
import pymysql
import pandas as pd


# 디비 정보 
news_title_db = pymysql.connect(
    user='', 
    passwd='', 
    host='', 
    db='', 
    charset=''
)

# DB 와 상호작용하기 위한 cursor 객체 생성
cursor = news_title_db.cursor(pymysql.cursors.DictCursor)


# 크롤링
url = "https://news.naver.com/main/list.naver?mode=LSD&mid=sec&sid1=001"
headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Safari/537.36"}
res = requests.get(url, headers=headers)
res.raise_for_status()

soup = BeautifulSoup(res.text, "lxml")

print("[뉴스 속보 헤드라인 가져오기]")
print()
news = soup.find_all("a", attrs={"class":"nclicks(fls.list)"})


i = 0
for new in news:
    text = new.get_text()
    hreflink = new["href"]
    text = text.lstrip()
    text = text.rstrip()
    text = text.replace("'", "")   # ' 문자열 제거
    text = text.replace('"', "")   # " 문자열 제거

    if(len(text) > 0) :
        i += 1 

        # 디비 저장
        sql = "INSERT INTO news_title(title, hreflink) VALUES('" + text + "', '" + hreflink + "');"
        cursor.execute(sql)
        news_title_db.commit()


# SELECT
sql = "SELECT * FROM news_title order by uid desc;"
cursor.execute(sql)
result = cursor.fetchall()

result = pd.DataFrame(result)
print(result)



'''
headtext = news[0].find("a", attrs={"class":"nclicks(fls.list)"})
headtext = headtext.find("img")["alt"]
print(headtext)
'''

