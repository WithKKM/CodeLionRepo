
import requests
import json


city = "Seoul"
apikey = "b136a73a2ff92e15bd1a9f42d0c87de7"
lang = "kr"
api = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={apikey}&lang={lang}&units=metric"

# print(api)

result = requests.get(api)


data = json.loads(result.text)
# print(type(data))

print(data["name"],"의 날씨입니다.")
print("날씨는",data["weather"][0]["description"],"입니다")
# weather 키 값은 list안에 dictionary가 있음
print("현재 온도는",data["main"]["temp"],"도 입니다")
print("체감 온도는",data["main"]["feels_like"],"도 입니다")
print("최저 기온은 ",data["main"]["temp_min"],"입니다.")
print("최고 기온은 ",data["main"]["temp_max"],"입니다.")
print("습도는 ",data["main"]["humidity"],"입니다.")
print("기압은 ",data["main"]["pressure"],"입니다.")
print("풍향은 ",data["wind"]["deg"],"입니다.")
print("풍속은 ",data["wind"]["speed"],"입니다.")


# API(Application Programming Interface)란: 프로그램과 프로그램을 이어주는 연결고리
# interface => 두 가지 이상의 것을 이어주는 연결 고리
# API Key = 방명록, 사용자 식별용 키
# Parameter : 함수에서 필요한 재료들
# f-string : 변수를 문자열로 인식하게 해주는 파이썬 기능
# json(javascript object notation) : javascript문법에 따르는 문자 포맷 (데이터를 주고 받을 때 사용하는 포맷)
# json 사용법: json.loads(str) => data타입이 바뀜