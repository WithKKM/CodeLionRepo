from bs4 import BeautifulSoup
import requests
from datetime import datetime

headers = {'User-Agent':'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36'}
url = "http://www.daum.net/"
response = requests.get(url,headers=headers)

soup = BeautifulSoup(response.text, 'html.parser')
rank = 1

results = soup.findAll('a','link_favorsch')

search_rank_file = open("rankresult.txt","a")

print(datetime.today().strftime("%Y년 %m월 %d일의 실시간 검색어 순위입니다.\n"))

for result in results:
    search_rank_file.write(str(rank)+"위:"+result.get_text()+"\n")
    print(rank,"위 : ",result.get_text(),"\n")
    rank += 1

# 웹 크롤러: 웹페이지의 데이터를 모아주는 소프트웨어
# 웹 크롤링: 크롤러로 웹페이지의 데이터를 추출해내는 행위
# 함수: 자주 사용하는 코드들을 묶어 놓고 사용할 수 있게 하는 것
# 모듈: 함수들의 모임, 자주 쓰는 함수들을 모아놓은 파일
# requests.get(url) = requests 모듈에 있는 get 함수가 url을 재료로 요청을 보냄.
# beautifulsoup: 가져온 데이터를 의미 있게 변경하는 것을 도와줌.(Parsing을 도와줌)
# Parsing: 데이터를 의미있게 변경, 뭉쳐져 있는 문자열을 분해해 의미 있는 데이터로 변경
# print(soup.findAll("a","link_favorsch")) : a태그와 link_favorsch가 포함된 태그들만 출력