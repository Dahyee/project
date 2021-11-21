'''
쿠팡 크롤링하기 2
'''
import requests
import re
from bs4 import BeautifulSoup

# 변경 X
headers = {"User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Safari/537.36"}

# 최근 1페이지 ~ 5페이지의 정보 가져오기

for i in range(1, 6):
    print("[{} 페이지]".format(i))

    url = "https://www.coupang.com/np/search?q=%EB%85%B8%ED%8A%B8%EB%B6%81&channel=user&component=&eventCategory=SRP&trcid=&traid=&sorter=scoreDesc&minPrice=&maxPrice=&priceRange=&filterType=&listSize=36&filter=&isPriceRange=false&brand=&offerCondition=&rating=0&page={}&rocketAll=false&searchIndexingToken=1=5&backgroundColor=".format(i)
    res = requests.get(url, headers=headers)
    res.raise_for_status()
    soup = BeautifulSoup(res.text, "lxml")


    items = soup.find_all("li", attrs={"class":re.compile("^search-product")})

    for item in items:

        # 광고 제품은 제외
        ad_badge = item.find("span", attrs={"class":"ad-badge-text"})
        if ad_badge:
            # print("<광고 상품 제외합니다.>")
            continue


        # 제품명
        name = item.find("div", attrs={"class":"name"}).get_text() 

        # 가격
        price = item.find("strong", attrs={"class":"price-value"}).get_text() 

        # 평점
        rate = item.find("em", attrs={"class":"rating"}) 
        if rate: # AttributeError: 'NoneType' object has no attribute 'get_text'
            rate = rate.get_text()
        else:
            rate = "평점 없음"
            # print("<평점 없는 상품 제외합니다.>")
            continue
        
        # 평점 수
        rate_count = item.find("span", attrs={"class":"rating-total-count"}) 
        if rate_count:
            rate_count = rate_count.get_text() # 출력값 : (리뷰수)
            rate_count = rate_count[1:-1]
        else:
            rate_count = "평점 수 없음"
            # print("<평점 없는 상품 제외합니다.>")
            continue

        # 링크 정보
        link = item.find("a", attrs={"class":"search-product-link"})["href"]


        # 조건1. : 리뷰 100개 이상, 평점 4.5 이상 되는 것만 가져오기
        if float(rate) >= 4.5 and int(rate_count) >= 100:
            print(f"제품명 : {name}")
            print(f"가격 : {price}")
            print(f"평점 : {rate}점 ({rate_count})")
            print("바로가기 : {}".format("https://www.coupang.com" + link))
            print("-"*50)

        # 조건2. : Apple 제품은 제외하고 가져오기
        if "Apple" in name:
            # print("<Apple 상품 제외합니다.>")
            continue

    print()



