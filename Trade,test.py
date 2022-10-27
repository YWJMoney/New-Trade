import pyupbit
import time

access = ""
secret = ""

def get_balance(ticker):
    balances = upbit.get_balances()
    for b in balances:
        if b['currency'] == ticker:
            if b['balance'] is not None:
                return float(b['balance'])
            else:
                return 0
    return 0

def get_target_price(price, k):
    search = pyupbit.get_ohlcv(price, interval="day", count=2)   # 목표가 설정
    target_price = df.iloc[0]['close'] * k           

def bull_market(ticker):
    df = pyupbit.get_ohlcv(ticker)
    ma5 = df['close'].rolling(window=30).mean()
    price = pyupbit.get_current_price(ticker)
    last_ma5 = ma5[-2]

    if price > last_ma5:
        return True
    else:
        return False
    
upbit = pyupbit.Upbit(access, secret)                 # 로그인
print("autotrade start")

while True:
    try:
        tickers = pyupbit.get_tickers(fiat="KRW")       # 한국 코인들의 모든 종류를 불러온다.
        df = tickers  

        price = pyupbit.get_current_price(tickers)      # 한국 코인의 현재가.
        
        price = pyupbit.get_tickers()                   # 모든 한국 코인의 5일 이동평균선을 가지고 상승장 파악
        for price in price:
            is_bull = bull_market(price)
            if is_bull:
                pass
            else:
                pass

        target_price = get_target_price(price, 1.03)    # 코인의 종가에 1.03을 곱한 것이 목표가다.

        if target_price < price and is_bull < price:    # 현재가가 목표값보다 크고 상승장일시 구매
            krw = get_balance("KRW")                    # 가지고 있는 현금이 5000원 이상일 시 구매
            if krw > 5000:
                upbit.buy_market_order(price, krw*0.05) # 전체 금액중 하나의 코인 구매 할 수 있는것은 5%
        else:
            btc = get_balance(price)
            if btc > target_price * 1.03 or btc > target_price * 0.96:
                upbit.sell_market_order(price, btc*0.9995)   
        time.sleep(1)
    except Exception as e:
        print(e)
        time.sleep(1)

    







    
    













