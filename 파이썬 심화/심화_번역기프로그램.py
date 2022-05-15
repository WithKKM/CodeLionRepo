from googletrans import Translator

translator = Translator()
# 번역기를 만든다

# sentence = "안녕하세요 코드라이언입니다."
sentence = input("번역을 원하는 문장을 입력해주세요 : ")
# # 언어 감지를 하고 싶은 문장을 설정
 

# # 언어 감지

# print(detected.lang)

dest = input("어떤 언어로 번역을 원하시나요?")
result = translator.translate(sentence,dest)
detected = translator.detect(sentence)

print("============출 력 결 과============")
print(detected.lang,":",sentence)
print(result.dest,":",result.text)
print("===================================")


# googletrans 모듈 : 언어 감지 및 번역을 도와주는 library(모듈의 모임)
# translate(text(번역을 원하는 문장),dest(어떤 언어로 번역할지),src(source의 준말, text재료의 언어를 작성해주는 공간, 선택적))