### 아웃백 스테이크 하우스 웹 페이지의 header 태그 추출 ###

import requests
from bs4 import BeautifulSox

url = 'https://www.outback.co.kr/'
response = requests.get(url)
html = response.text
soup = beautifulSoup(html, 'html.parser')

id_element = soup.find(id='dHead')
print(id_element)
print(id_element.text)



