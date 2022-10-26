import time
import pyupbit
import datetime

access = "ZxMPQ31ZfQkMnXhQ9zkAla1YoCh1laIiMpfgoYl4"
secret = "gcEWe7x1InB3mKRsmpMeNiKVnsdWCxDrkGbzlhR1"

def get_start_time(ticker):
    """시작 시간 조회"""
    df = pyupbit.get_ohlcv(ticker, interval="minute", count=1440) # OHLCV = O : 시작가, H : 고가, L : 저가, C : 종가, V: 거래량
    start_time = df.index[0]
    return start_time

def get_balance(ticker):
    """잔고 조회"""
    balances = upbit.get_balances()
    for b in balances:
        if b['currency'] == ticker:
            if b['balance'] is not None:
                return float(b['balance'])
            else:
                return 0
    return 0

def bull_market(ticker):    # 상승장을 구분하는 함수
    df = pyupbit.get_ohlcv(ticker)
    ma5 = df['close'].rolling(window=5).mean()
    price = pyupbit.get_current_price(ticker)
    last_ma5 = ma5[-2]

    if price > last_ma5:
        return True
    else:
        return False
        
tickers = pyupbit.get_tickers()   # 상승장을 구분하는 함수
for tickers in tickers:
    is_bull = bull_market(tickers)
    if is_bull:
        pass
    else:
        pass

def get_current_price(ticker):
    """현재가 조회"""
    return pyupbit.get_orderbook(ticker=ticker)["orderbook_units"][0]["ask_price"]

def get_target_price(ticker):
    """변동성 돌파 전략으로 매수 목표가 조회"""
    df = pyupbit.get_ohlcv(ticker, interval="minute", count=1440) # OHLCV = O : 시작가, H : 고가, L : 저가, C : 종가, V: 거래량
    target_price = df.iloc[0]['close'] * 1.03 # iloc = 데이터 선택 해서 변동성 돌파 전략 구성
    return target_price # 목표가는 리턴한다.

# 로그인
upbit = pyupbit.Upbit(access, secret)
print("autotrade start")

# 자동매매 시작
while True: 
    try:
        target_price = get_target_price("tickers")
        current_price = get_current_price("tickers")
        if target_price and is_bull:
            krw = get_balance("KRW")
            if krw > 5000:
              upbit.buy_market_order("tickers", krw*0.01)
        else:
            ticker = get_balance("tickers")
            if target_price * 1.06 >= current_price | target_price * 0.99 :
                if ticker :
                    upbit.sell_market_order("tickers", ticker*0.9995)
        time.sleep(1)
    except Exception as e:
        print(e)
        time.sleep(1)   