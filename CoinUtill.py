
import uuid
import jwt
import requests
from Log import *
#기초 고정값 세팅 객체

class CoinUtill:
    #기본 고정값 세팅 
    def __init__(self):
        #self.access_key = "PaYjlkxaG9pCorYxxNA896LYGfx1I18nXhMKaTjA"
        #self.secret_key = "O6dc1x8RVJ4xZLQFOtyGql6IxOWvjTxtypxnjDbm"
        #우분투용
        self.access_key = "sCkRMzkG0Bt9dxxLboWRlNmi983qydxGqxHxzMGo"
        self.secret_key = "kw6tRqwVJYI4sttxKytRC1IERbgaFIeHvsRHCDnf"
        
        self.requestURL = "https://api.upbit.com/v1/"
        self.limitMoney = 10000
        #라인 메신저 알림 토큰
        self.message_url = "https://notify-api.line.me/api/notify"
        self.lineMessageToken = "BgWBqobOZRydM7qoXXRBxCr2B5Dm1spn4c1U7RSD0kc"
        #기준3만원씩 투자 
        self.orderMoney = 20000

        #익절 퍼센트 
        self.sellPercent  = 1.1
        #손절 퍼센트
        self.minusPercent = -1

        #익절 퍼센트 100원 이하 1프로 
        self.sellPercentSecond = 1

        #손절 퍼센트 100원 이하 -2프로
        self.minusPercentSecond = -0.9
        
    #토큰값 가져오기 
    def get_authHeader(self):
        payload = {
                'access_key' : self.access_key,
                'nonce': str(uuid.uuid4())
            }
        
        jwt_token = jwt.encode(payload,self.secret_key)
        authorize_token = 'Bearer {}'.format(jwt_token)
        headers = {"Authorization": authorize_token}
        return headers

    #라인 메신저 보내기
    def send_message(self,message):
        log = Log().initLogger()

        response = requests.post(
            self.message_url,
            headers={
                'Authorization' : 'Bearer ' + self.lineMessageToken
            },
            data = {
                'message' : message
            }
        )
        log.debug("라인>>>"+response.text)

    #init 변수 리턴
    def get_requestURL(self):
        return self.requestURL    

    def get_accessKey(self):
        return self.access_key 

    def get_secretKey(self):
        return self.secret_key 
        
    def get_limitMoney(self):
        return self.limitMoney
    
    def get_sellPercent(self):
        return self.sellPercent

    def get_minusPercent(self):
        return self.minusPercent

    def get_orderMoney(self):
        return self.orderMoney

    def get_secondSellPercent(self):
        return self.minusPercentSecond    

    def get_minusPercentSecond(self):
        return self.minusPercentSecond    

    def get_sellPercentSecond(self):
        return self.sellPercentSecond    