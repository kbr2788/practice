import requests
from bs4 import BeautifulSoup
import urllib.parse as urlparser

#urlparser의 quote함수를 이용해서 한글을 utf-8로 인코딩
keyword = '코로나'
url = 'https://search.naver.com/search.naver?sm=top_hty&fbm=1&ie=utf8&query=' + urlparser.quote(keyword)

response = requests.get(url)

#Document Object Model
dom = BeautifulSoup(response.text, 'html.parser')
#dom

#CSS selector - 해당 CSS selector를 이용하여 선택된 모든 엘리먼트를 리스트 타입으로 리턴한다.
related_search = dom.select('#nx_related_keywords ul._related_keyword_ul li')
#print(related_search)
#print(len(related_search))

#원하는 데이터만 선택하여 리스트에 저장
[
    i.text.strip()
    for i in related_search
]

#출처
#https://blog.naver.com/PostView.nhn?blogId=swon7824&logNo=222039472386&categoryNo=26&parentCategoryNo=0&viewDate=&currentPage=2&postListTopCurrentPage=1&from=search&userTopListOpen=true&userTopListCount=5&userTopListManageOpen=false&userTopListCurrentPage=2