import urllib.request
from bs4 import BeautifulSoup

url = 'https://search.naver.com/search.naver?where=post&sm=tab_jum&query=%EC%B0%A8%EB%B0%95%ED%9B%84%EA%B8%B0'
html = urllib.request.urlopen(url).read()
soup = BeautifulSoup(html, 'html.parser')

title = soup.find_all(class_='sh_blog_title')
#print(title)

for i in title:
    print(i.attrs['title'])
    print(i.attrs['href'])
    print()

#출처
#https://kimflstudio.tistory.com/entry/%ED%8C%8C%EC%9D%B4%EC%8D%AC-beautifulsoup-%ED%81%AC%EB%A1%A4%EB%A7%81-%EC%98%88%EC%A0%9C-%EB%84%A4%EC%9D%B4%EB%B2%84-%EB%B8%94%EB%A1%9C%EA%B7%B8-%EA%B2%80%EC%83%89%EA%B2%B0%EA%B3%BC-%ED%81%AC%EB%A1%A4%EB%9F%AC-%EB%A7%8C%EB%93%A4%EA%B8%B0-1%ED%8E%B8?category=774840
