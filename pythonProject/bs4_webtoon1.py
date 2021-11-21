'''
네이버 웹툰 크롤링하기 1
'''

import requests
from bs4 import BeautifulSoup

url = "https://comic.naver.com/webtoon/weekday"
res = requests.get(url)
res.raise_for_status()                   # 오류 발생 시 프로그램 종료

# 받아온 text를 lxml 을 통해 bs 객체로 만들기
soup = BeautifulSoup(res.text, "lxml")


# title 태그 정보 가져오기
print("[title 태그 정보]")
print(soup.title)
print()

print("[title 태그 안의 텍스트 정보]")
print(soup.title.get_text())
print()


# a 태그 정보 가져오기
print("[a 태그 정보]")
print(soup.a)
print()

print("[a 태그의 속성 정보]")
print(soup.a.attrs)
print()

print("[a 태그의 속성 중 href 정보]")
print(soup.a["href"])
print()


# 랭킹 1위 웹툰 가져오기
print("[랭킹 1위 웹툰 정보]")
print(soup.find("li", attrs={"class":"rank01"}))
print()

print("[랭킹 1위 웹툰의 링크 정보]")
rank1 = soup.find("li", attrs={"class":"rank01"})
print(rank1.a)
print()

print("[랭킹 1위의 제목을 이용하여 링크 정보 출력]")
webtoon = soup.find("a", text="상위1%-6화")
print(webtoon)
print()


# 형제태그 활용하여 랭킹 웹툰 가져오기
print("[랭킹 1위 웹툰 제목]")
rank1 = soup.find("li", attrs={"class":"rank01"})
print(rank1.a.get_text())
print()

print("[랭킹 2위 웹툰 제목]")
rank2 = rank1.next_sibling.next_sibling
# rank2 = rank1.find_next_sibling("li")
print(rank2.a.get_text())
print()

print("[랭킹 3위 제목]")
rank3 = rank2.next_sibling.next_sibling
print(rank3.a.get_text())
print()

print("[랭킹 2위 제목]")
rank2 = rank3.previous_sibling.previous_sibling
# rank2 = rank3.find_previous_sibling("li")
print(rank2.a.get_text())
print()


# 부모 태그 모두 가져오기
print("[부모 태그 모두 가져오기]")
print(rank1.parent)
print()


# 다음 형제들을 모두 가져오기
print("[형제 태그 모두 가져오기]")
print(rank1.find_next_siblings("li"))
print()



