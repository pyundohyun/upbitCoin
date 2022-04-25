# Access keyf2AMzohDIQ7vZrkpZixOgT9mToDkqnlUtzmnh91Z
# Secret keyol30HjiAx4hTi6p2K3xVpTYr45VcjtfebxWiFW2L
# 편도현

from time import sleep
import pyupbit
from datetime import datetime, timedelta


from CoinUtill import *
from CoinEvent import *
from Strategy import *
from Log import *
import asyncio

import os



#dfTomorrow = pyupbit.get_ohlcv("KRW-BTC", interval="minute5", to=tomorrow)
#print(dfTomorrow)

#CoinUtill 객체 선언
CoinUtill = CoinUtill()
CoinEvent = CoinEvent()
Strategy  = Strategy()

#티커조회 
#FIAT 종류 KRW/BTC/ETH/USDT
tickers = pyupbit.get_tickers(fiat="KRW")
#print(tickers)
# print(CoinEvent.checkBuyCoin("KWm"))

#print('현재 보유 잔액>>>'+str(CoinEvent.getMyChongal()))


#print(CoinEvent.allSelCoin())

#현재 내잔고
#print(CoinEvent.get_myBalance())
#현재 가격 
#print(CoinEvent.get_cur_info())
async def findCoin():
    

    cnt = 1

    log = Log().initLogger()
  
    while(True):


        # while(True):
        curTime = (datetime.today()).strftime("%Y%m%d %H:%M:%S")
        endTime = (datetime.today()).strftime("%H%M")
        
        #print('[[[[[[[[[편도 '+ str(cnt) +' 회전시작::: '+ str(curTime) +']]]]]]]]]')
        #print("  ")

        log.debug('[[[[[[[[[탕스 '+ str(cnt) +' 회전시작::: '+ str(curTime) +']]]]]]]]]')
        log.debug("  ")
        CoinUtill.send_message("[[[[[[[[[탕스 "+ str(cnt) +" 회전시작::: "+ str(curTime) +"]]]]]]]]]")

        #오전 8시 ~ 9시에 전량매도 
        if(int(endTime) < 900 and int(endTime) > 845):
            CoinEvent.allSelCoin()
            await asyncio.sleep(10) 
            #손익분기 추출해서 엑셀저장
            curTM = (datetime.today()).strftime("%Y%m%d")+str("0900")
            beforeTM = (datetime.today() - timedelta(1)).strftime("%Y%m%d")+str("0900")

            #손익분기 엑셀안만들어졌으면 만듬
            if(os.path.isfile("profitAndSell_"+beforeTM+"_"+curTM+".xlsx") == False):
                try :
                   CoinEvent.getMyPaymentList()      
                except Exception as Err:
                    log.debug('[[[[[[Error]]]]]] getMyPaymentList Error>>>'+str(Err))
        # elif(int(endTime) < 830 and int(endTime) > 800):
        #     #log.debug('휴식시간---------------- 8시 ~~~ 8시 53분')
        #     print("휴식시간")
        else :
            
            # 내가만든 짬뽕전략
            # for item in tickers:
            #     #상승량 높은것만 추려서 확인
            #     if(await Strategy.get_bigShort_coinList(item)):
            #         #구매 코인찾기 둘다 비동기로 돌게함
            #         await Strategy.goFindCoin(item)
            #         #await asyncio.sleep(0.2)
            #     #현재 구매 코인팔가격인지 확인
            #     await Strategy.checkSellMyCoin(item)

            #sleep(0.3)
            
            #변동성 돌파전략으로 진행
            for item in tickers:
                # 400억 이상 누적 거래대금 + -7 ~ 10 전일대비  or 보유코인
                if(await Strategy.get_bigShort_coinList(item)):
                   #CoinUtill.send_message("[[[[[[[[[ 0 이상 코인::: "+str(item)+"]]]]]]]]]")
                   Strategy.goBuyCoin(item)

#        log.debug("  ")
#        log.debug('[[[[[[[[[ 회전끝::: '+str(curTime)+']]]]]]]]]')
         
        #CoinUtill.send_message("[[[[[[[[[ 회전끝::: "+str(curTime)+"]]]]]]]]]")

        #print("  ")
        #print('[[[[[[[[[ 회전끝::: '+str(curTime)+']]]]]]]]]')
        #sleep(60) #5초마다 돌게 

        cnt = cnt+1
        # #sleep(500)

#비동기로 쓰려면 비동기 함수 처리필요 
async def process_async():
    await asyncio.wait([
        findCoin(),
    ])

#메인함수
if __name__ == '__main__':
    asyncio.run(process_async())