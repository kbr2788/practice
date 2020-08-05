import requests
from bs4 import BeautifulSoup
import urllib.parse as urlparser

def naver_related_search(keyword):
    url = 'https://search.naver.com/search.naver?sm=top_hty&fbm=1&ie=utf8&query=' + urlparser.quote(keyword)
    response = requests.get(url)
    
    if response.status_code != 200:
        return '실패'
    else:
        dom = BeautifulSoup(response.text, 'html.parser')
        related_search = dom.select('#nx_related_keywords ul._related_keyword_ul li')
        result = [
            i.text.strip()
            for i in related_search
        ]
        return result

naver_related_search('코로나')

#출처
#https://blog.naver.com/PostView.nhn?blogId=swon7824&logNo=222039472386&categoryNo=26&parentCategoryNo=0&viewDate=&currentPage=2&postListTopCurrentPage=1&from=search&userTopListOpen=true&userTopListCount=5&userTopListManageOpen=false&userTopListCurrentPage=2