import requests

#해당 url 준비하기
url = 'https://apis.naver.com/mobile_main/srchrank/srchrank?frm=main&ag=20s&gr=1&ma=-1&si=-1&en=-1&sp=-1'

#requests 보내기 
response = requests.get(url)

#데이터 확인
response.text

#python 데이터로 변환하기 (list,dict)
data = response.json()

#데이터 확인
#data

#원하는 데이터 추출하기
rank_data = data['data']

[
    str(i['rank'])+ '. ' + i['keyword'] 
    for i in rank_data
]


#출처 
#https://blog.naver.com/PostView.nhn?blogId=swon7824&logNo=222039857687&parentCategoryNo=&categoryNo=26&viewDate=&isShowPopularPosts=true&from=search