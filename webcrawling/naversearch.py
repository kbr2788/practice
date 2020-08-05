import requests

url = 'https://apis.naver.com/mobile_main/srchrank/srchrank?frm=main&ag=20s&gr=1&ma=-1&si=-1&en=-1&sp=-1'

#requests 보내기 
response = requests.get(url)

#데이터 확인
response.text