import smtplib
from email.message import EmailMessage
import imghdr
# imghdr: 이미지 확장자를 판단
import re


SMTP_SERVER = "smtp.gmail.com"
SMTP_PORT = 465
# Gmail에서 지정한 포트 번호



def sendEmail(addr):
    reg = "^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9]+\.[a-zA-Z]{2,3}$"
    if bool(re.match(reg,addr)):
         smtp.send_message(message)
         print("정상적으로 메일이 발송되었습니다")
    else:
        print("유효한 이메일 주소가 아닙니다.")

message = EmailMessage()
# EmailMessage라는 기능이 알아서 Email을 담을 수 있는 통을 만들어 message 변수에 넣어줌

message.set_content("코드라이언 심화 과정입니다.")
# 본문 내용

message["Subject"] = "이것은 제목입니다"
message["From"] = "cu4149@likelion.org"
message["To"] = "cu4149@gmail.com"
# MIME-Header: Subject, from, to로 구성
# MIME-Header에 들어가는 값이기 때문에 [](대괄호)로 지정해야 함.

with open("연두 사진.jpg","rb") as image:
    image_file = image.read()
# close문 없이도 열었던 파일을 모두 사용한 뒤 자동으로 닫음

image_type = imghdr.what('연두 사진',image_file)
# what함수는 파일명, 실제 파일 재료가 필요함.
message.add_attachment(image_file,maintype='image',subtype=image_type)


smtp = smtplib.SMTP_SSL(SMTP_SERVER,SMTP_PORT)
# Gmail서버는 보안 문제로 SSL을 필수적으로 요구함
# SSL = 아무나 서버에 접근할 수 없도록 막아주는 암호화 방식

smtp.login("cu4149@likelion.org","rkdals050$")

sendEmail("cu4149@likelion.org")
# 정규표현식으로 유효성 검사 함수 사용


smtp.send_message(message)
# 보내는 Email을 message에 넣어놨기 때문에 재료로 message 사용

smtp.quit()






# IMAP: 다양한 기기에서 이메일에 액세스하고 클라이언트 서버에 이메일과 첨부 파일을 저장하기 위함
# SMTP: Simple Mail Transfer Protocol, 간단하게 메일을 보내기 위한 약속
# SMTP동작 원리: (1)Email Client가 '메일을 보낸다'라는 신호를 주면 메일은 Email Server(나의Gmail서버)로 도달, 이 때 사용되는 것이 SMTP
#               (2)내 email서버에서 상대방 email서버로 메일을 보낼 때 사용하는 것도 SMTP
#               (3)IMAP은 다른 서버에서 가져온 메일을 Email Client로 보냄
# SMTP 서버를 이용해서 우리가 원하는 곳으로 메일을 보낼 수 있다.
# SMTP Server ex: Address: smtp.gmail.com / Port: 465
# smtplib: SMTP를 쉽게 이용할 수 있게 만드는 라이브러리
# SMTP 절차 (1) SMTP 메일 서버를 연결한다: 
#           (2) SMTP 메일 서버에 로그인한다
#           (3) SMTP 메일 서버로 메일을 보낸다.
# MIME: 한글 지원 안되는 smtp서버로 한글을 보내기 위한 장치, email.message모듈 사용
# 바이너리: 컴퓨터가 읽을 수 있는 언어로 변경한 것
# add_attachment(): 텍스트가 아닌 다른 파일들을 첨부할 때 사용하는 기능
# 유효성 검사: 보내고자 하는 메일 주소가 진짜가 맞는지 유효성을 확인
# 이메일 정규표현식: 이메일에만 나타나는 특정 패턴을 조건으로 주고 메일이 적합한지 판단함으로써 유효성 검사 가능