#네이버 실시간 검색어 파싱
# -*- coding: utf-8 -*-
import requests
from bs4 import BeautifulSoup as bsp


session=requests.session()
url="http://naver.com"
req1=session.get(url)

soup=bsp(req1.text,'html5lib')

rank= soup.find_all("span","ah_r")
rank2= soup.find_all("span","ah_k")

print("===실시간 검색어===")
for i in range(10):
    print (rank2[i].text)

print("===실시간 검색어===")
