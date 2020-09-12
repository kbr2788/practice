import urllib.request
from bs4 import BeautifulSoup
from urllib import parse
import ssl

context = ssl._create_unverified_context()
search = input("검색어를 입력하세요 : ")
baseUrl1 = "https://search.naver.com/search.naver?date_from=&date_option=0&date_to=&dup_remove=1&nso=&post_blogurl=&post_blogurl_without=&query=" 
baseUrl2 = "&sm=tab_pge&srchby=all&st=sim&where=post&start="
postNum = 1

for i in range(5): #몇페이지 출력할지
    newUrl = baseUrl1+parse.quote_plus(search)+baseUrl2+str(postNum)
    html = urllib.request.urlopen(newUrl,context=context).read()
    soup = BeautifulSoup(html, 'html.parser')
    title = soup.find_all(class_='sh_blog_title')
    #print(title)
    postNum = postNum+10
    for i in title:
        print(i.attrs['title'])
        print(i.attrs['href'])
        print()
