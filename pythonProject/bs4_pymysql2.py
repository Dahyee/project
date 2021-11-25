'''
네이버 뉴스 >> 기업 검색 후 기업별 뉴스 가져오기
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


# 검색할 키워드 저장되어있는 테이블에서 키워드 SELECT 하기(테스트 10개)
sql = "SELECT code, keyword FROM keyword limit 10;"
cursor.execute(sql)
result = cursor.fetchall()

result = pd.DataFrame(result, columns=['code', 'keyword'])
result = result.values.tolist()     # list 값으로 바꾸기
print(result)


# 키워드별로 크롤링
for i in range(0, len(result)):
    url = "https://search.naver.com/search.naver?where=news&sm=tab_pge&query="+ result[i][1] +"&sort=0&photo=0&field=0&pd=0&ds=&de=&cluster_rank=22&mynews=0&office_type=0&office_section_code=0&news_office_checked=&nso=so:r,p:all,a:all&start=1"
    headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Safari/537.36"}
    res = requests.get(url, headers=headers)
    res.raise_for_status()
    soup = BeautifulSoup(res.text, "lxml")

    text = soup.find_all("a", attrs={"class":"news_tit"})

    for title in text:
        href = title["href"]
        news_title = title["title"] 
        news_title = news_title.replace("'", "")
        news_title = news_title.replace('"', "")
        href = title["href"]

        # 디비 저장
        sql = "INSERT INTO news_title(code, keyword, title, hreflink) VALUES({}, '{}', '{}', '{}');".format(result[i][0], result[i][1], news_title, href)
        cursor.execute(sql)
        news_title_db.commit()
    
    print()
