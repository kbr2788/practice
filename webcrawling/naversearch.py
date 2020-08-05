import requests

url = 'https://apis.naver.com/mobile_main/srchrank/srchrank?frm=main&ag=20s&gr=1&ma=-1&si=-1&en=-1&sp=-1'

response = requests.get(url)

response.text