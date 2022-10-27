import time
import pyupbit
import datetime

access = "ZxMPQ31ZfQkMnXhQ9zkAla1YoCh1laIiMpfgoYl4"
secret = "gcEWe7x1InB3mKRsmpMeNiKVnsdWCxDrkGbzlhR1"

def get_target_price(ticker, k):
    """변동성 돌파 전략으로 매수 목표가 조회"""
    df = pyupbit.get_ohlcv(ticker, interval="day", count=1) # OHLCV = O : 시작가, H : 고가, L : 저가, C : 종가, V: 거래량
    target_price = df.iloc[0]['close'] * k # iloc = 데이터 선택 해서 변동성 돌파 전략 구성
    return target_price # 목표가는 리턴한다.

def get_start_time(ticker):
    """시작 시간 조회"""
    df = pyupbit.get_ohlcv(ticker, interval="day", count=2) # OHLCV = O : 시작가, H : 고가, L : 저가, C : 종가, V: 거래량
    start_time = df.index[0]
    return start_time

def get_ma5(ticker):
    """5일 이동 평균선 조회"""
    df = pyupbit.get_ohlcv(ticker, interval="day", count=5)
    ma5 = df['close'].rolling(5).mean().iloc[-1]
    return ma5

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

def get_current_price(ticker):
    """현재가 조회"""
    return pyupbit.get_orderbook(ticker=ticker)["orderbook_units"][0]["ask_price"]

# 로그인
upbit = pyupbit.Upbit(access, secret)
print("autotrade start")

# 자동매매 시작
while True: 
    try:
        now = datetime.datetime.now()
        start_time = get_start_time("KRW-BTC")
        end_time = start_time + datetime.timedelta(days=1)

        if start_time < now < end_time - datetime.timedelta(seconds=10):
            target_price = get_target_price("KRW-BTC, KRW-ETH, KRW-NEO, KRW-MTL, KRW-XRP, KRW-ETC, KRW-OMG, KRW-SN, KRW-WAVES, KRW-XEM, KRW-QTUM, KRW-LSK, KRW-STEEM, KRW-XLM, KRW-ARDR, KRW-ARK, KRW-STORJ, KRW-GRS, KRW-REP, KRW-ADA, KRW-SBD, KRW-POWR, KRW-BTG, KRW-ICX, KRW-EOS, KRW-TRX, KRW-SC, KRW-ONT, KRW-ZIL, KRW-POLY, KRW-ZRX, KRW-LOOM, KRW-BCH, KRW-BAT, 'KRW-IOST, KRW-RFR, KRW-CVC, KRW-IQ, KRW-IOTA, KRW-MFT, KRW-ONG, KRW-GAS, KRW-UPP, KRW-ELF, KRW-KNC, KRW-BSV, KRW-THETA, KRW-QKC, KRW-BTT, KRW-MOC, KRW-ENJ, KRW-TFUEL, KRW-MANA, KRW-ANKR, KRW-AERGO, KRW-ATOM, KRW-TT, KRW-CRE, KRW-MBL, KRW-WAXP, KRW-HBAR, KRW-MED, KRW-MLK, KRW-STPT, KRW-ORBS, KRW-VET, KRW-CHZ, KRW-STMX, KRW-DKA, KRW-HIVE, KRW-KAVA, KRW-AHT, KRW-LINK, KRW-XTZ, KRW-BORA, KRW-JST, KRW-CRO, KRW-TON, KRW-SXP, KRW-HUNT, KRW-PLA, KRW-DOT, KRW-SRM, KRW-MVL, KRW-STRAX, KRW-AQT, KRW-GLM, KRW-SSX, KRW-META, KRW-FCT2, KRW-CBK, KRW-SAND, KRW-HUM, KRW-DOGE, KRW-STRK, KRW-PUNDIX, KRW-FLOW, KRW-DAWN, KRW-AXS, KRW-STX, KRW-XEC, KRW-SOL, KRW-MATIC, KRW-NU, KRW-AAVE, KRW-1INCH, KRW-ALGO, KRW-NEAR, KRW-WEMIX, KRW-AVAX, KRW-T, KRW-CELO, KRW-GMT, KRW-APT" , 1.03)
            current_price = get_current_price("KRW-BTC, KRW-ETH, KRW-NEO, KRW-MTL, KRW-XRP, KRW-ETC, KRW-OMG, KRW-SN, KRW-WAVES, KRW-XEM, KRW-QTUM, KRW-LSK, KRW-STEEM, KRW-XLM, KRW-ARDR, KRW-ARK, KRW-STORJ, KRW-GRS, KRW-REP, KRW-ADA, KRW-SBD, KRW-POWR, KRW-BTG, KRW-ICX, KRW-EOS, KRW-TRX, KRW-SC, KRW-ONT, KRW-ZIL, KRW-POLY, KRW-ZRX, KRW-LOOM, KRW-BCH, KRW-BAT, 'KRW-IOST, KRW-RFR, KRW-CVC, KRW-IQ, KRW-IOTA, KRW-MFT, KRW-ONG, KRW-GAS, KRW-UPP, KRW-ELF, KRW-KNC, KRW-BSV, KRW-THETA, KRW-QKC, KRW-BTT, KRW-MOC, KRW-ENJ, KRW-TFUEL, KRW-MANA, KRW-ANKR, KRW-AERGO, KRW-ATOM, KRW-TT, KRW-CRE, KRW-MBL, KRW-WAXP, KRW-HBAR, KRW-MED, KRW-MLK, KRW-STPT, KRW-ORBS, KRW-VET, KRW-CHZ, KRW-STMX, KRW-DKA, KRW-HIVE, KRW-KAVA, KRW-AHT, KRW-LINK, KRW-XTZ, KRW-BORA, KRW-JST, KRW-CRO, KRW-TON, KRW-SXP, KRW-HUNT, KRW-PLA, KRW-DOT, KRW-SRM, KRW-MVL, KRW-STRAX, KRW-AQT, KRW-GLM, KRW-SSX, KRW-META, KRW-FCT2, KRW-CBK, KRW-SAND, KRW-HUM, KRW-DOGE, KRW-STRK, KRW-PUNDIX, KRW-FLOW, KRW-DAWN, KRW-AXS, KRW-STX, KRW-XEC, KRW-SOL, KRW-MATIC, KRW-NU, KRW-AAVE, KRW-1INCH, KRW-ALGO, KRW-NEAR, KRW-WEMIX, KRW-AVAX, KRW-T, KRW-CELO, KRW-GMT, KRW-APT") 
            ma5 = get_ma5("KRW-BTC, KRW-ETH, KRW-NEO, KRW-MTL, KRW-XRP, KRW-ETC, KRW-OMG, KRW-SN, KRW-WAVES, KRW-XEM, KRW-QTUM, KRW-LSK, KRW-STEEM, KRW-XLM, KRW-ARDR, KRW-ARK, KRW-STORJ, KRW-GRS, KRW-REP, KRW-ADA, KRW-SBD, KRW-POWR, KRW-BTG, KRW-ICX, KRW-EOS, KRW-TRX, KRW-SC, KRW-ONT, KRW-ZIL, KRW-POLY, KRW-ZRX, KRW-LOOM, KRW-BCH, KRW-BAT, 'KRW-IOST, KRW-RFR, KRW-CVC, KRW-IQ, KRW-IOTA, KRW-MFT, KRW-ONG, KRW-GAS, KRW-UPP, KRW-ELF, KRW-KNC, KRW-BSV, KRW-THETA, KRW-QKC, KRW-BTT, KRW-MOC, KRW-ENJ, KRW-TFUEL, KRW-MANA, KRW-ANKR, KRW-AERGO, KRW-ATOM, KRW-TT, KRW-CRE, KRW-MBL, KRW-WAXP, KRW-HBAR, KRW-MED, KRW-MLK, KRW-STPT, KRW-ORBS, KRW-VET, KRW-CHZ, KRW-STMX, KRW-DKA, KRW-HIVE, KRW-KAVA, KRW-AHT, KRW-LINK, KRW-XTZ, KRW-BORA, KRW-JST, KRW-CRO, KRW-TON, KRW-SXP, KRW-HUNT, KRW-PLA, KRW-DOT, KRW-SRM, KRW-MVL, KRW-STRAX, KRW-AQT, KRW-GLM, KRW-SSX, KRW-META, KRW-FCT2, KRW-CBK, KRW-SAND, KRW-HUM, KRW-DOGE, KRW-STRK, KRW-PUNDIX, KRW-FLOW, KRW-DAWN, KRW-AXS, KRW-STX, KRW-XEC, KRW-SOL, KRW-MATIC, KRW-NU, KRW-AAVE, KRW-1INCH, KRW-ALGO, KRW-NEAR, KRW-WEMIX, KRW-AVAX, KRW-T, KRW-CELO, KRW-GMT, KRW-APT")
            if target_price < current_price and ma5 < current_price:
                krw = get_balance("BTC, ETH, NEO, MTL, XRP, ETC, OMG, SN, WAVES, XEM, QTUM, LSK, STEEM, XLM, ARDR, ARK, STORJ, GRS, REP, ADA, SBD, POWR, BTG, ICX, EOS, TRX, SC, ONT, ZIL, POLY, ZRX, LOOM, BCH, BAT, IOST, RFR, CVC, IQ, IOTA, MFT, ONG, GAS, UPP, ELF, KNC, BSV, THETA, QKC, BTT, MOC, ENJ, TFUEL, MANA, ANKR, AERGO, ATOM, TT, CRE, MBL, WAXP, HBAR, MED, MLK, STPT, ORBS, VET, CHZ, STMX, DKA, HIVE, KAVA, AHT, LINK, XTZ, BORA, JST, CRO, TON, SXP, HUNT, PLA, DOT, SRM, MVL, STRAX, AQT, GLM, SSX, META, FCT2, CBK, SAND, HUM, DOGE, STRK, PUNDIX, FLOW, DAWN, AXS, STX, XEC, SOL, MATIC, NU, AAVE, 1INCH, ALGO, NEAR, WEMIX, AVAX, T, CELO, GMT, APT")
                if krw > 5000:
                    upbit.buy_market_order("KRW-BTC, KRW-ETH, KRW-NEO, KRW-MTL, KRW-XRP, KRW-ETC, KRW-OMG, KRW-SN, KRW-WAVES, KRW-XEM, KRW-QTUM, KRW-LSK, KRW-STEEM, KRW-XLM, KRW-ARDR, KRW-ARK, KRW-STORJ, KRW-GRS, KRW-REP, KRW-ADA, KRW-SBD, KRW-POWR, KRW-BTG, KRW-ICX, KRW-EOS, KRW-TRX, KRW-SC, KRW-ONT, KRW-ZIL, KRW-POLY, KRW-ZRX, KRW-LOOM, KRW-BCH, KRW-BAT, 'KRW-IOST, KRW-RFR, KRW-CVC, KRW-IQ, KRW-IOTA, KRW-MFT, KRW-ONG, KRW-GAS, KRW-UPP, KRW-ELF, KRW-KNC, KRW-BSV, KRW-THETA, KRW-QKC, KRW-BTT, KRW-MOC, KRW-ENJ, KRW-TFUEL, KRW-MANA, KRW-ANKR, KRW-AERGO, KRW-ATOM, KRW-TT, KRW-CRE, KRW-MBL, KRW-WAXP, KRW-HBAR, KRW-MED, KRW-MLK, KRW-STPT, KRW-ORBS, KRW-VET, KRW-CHZ, KRW-STMX, KRW-DKA, KRW-HIVE, KRW-KAVA, KRW-AHT, KRW-LINK, KRW-XTZ, KRW-BORA, KRW-JST, KRW-CRO, KRW-TON, KRW-SXP, KRW-HUNT, KRW-PLA, KRW-DOT, KRW-SRM, KRW-MVL, KRW-STRAX, KRW-AQT, KRW-GLM, KRW-SSX, KRW-META, KRW-FCT2, KRW-CBK, KRW-SAND, KRW-HUM, KRW-DOGE, KRW-STRK, KRW-PUNDIX, KRW-FLOW, KRW-DAWN, KRW-AXS, KRW-STX, KRW-XEC, KRW-SOL, KRW-MATIC, KRW-NU, KRW-AAVE, KRW-1INCH, KRW-ALGO, KRW-NEAR, KRW-WEMIX, KRW-AVAX, KRW-T, KRW-CELO, KRW-GMT, KRW-APT", krw*0.05)
            else:
                btc = get_balance("BTC, ETH, NEO, MTL, XRP, ETC, OMG, SN, WAVES, XEM, QTUM, LSK, STEEM, XLM, ARDR, ARK, STORJ, GRS, REP, ADA, SBD, POWR, BTG, ICX, EOS, TRX, SC, ONT, ZIL, POLY, ZRX, LOOM, BCH, BAT, IOST, RFR, CVC, IQ, IOTA, MFT, ONG, GAS, UPP, ELF, KNC, BSV, THETA, QKC, BTT, MOC, ENJ, TFUEL, MANA, ANKR, AERGO, ATOM, TT, CRE, MBL, WAXP, HBAR, MED, MLK, STPT, ORBS, VET, CHZ, STMX, DKA, HIVE, KAVA, AHT, LINK, XTZ, BORA, JST, CRO, TON, SXP, HUNT, PLA, DOT, SRM, MVL, STRAX, AQT, GLM, SSX, META, FCT2, CBK, SAND, HUM, DOGE, STRK, PUNDIX, FLOW, DAWN, AXS, STX, XEC, SOL, MATIC, NU, AAVE, 1INCH, ALGO, NEAR, WEMIX, AVAX, T, CELO, GMT, APT")
                if btc > target_price * 1.03 or btc > target_price * 0.96:
                    upbit.sell_market_order("KRW-BTC, KRW-ETH, KRW-NEO, KRW-MTL, KRW-XRP, KRW-ETC, KRW-OMG, KRW-SN, KRW-WAVES, KRW-XEM, KRW-QTUM, KRW-LSK, KRW-STEEM, KRW-XLM, KRW-ARDR, KRW-ARK, KRW-STORJ, KRW-GRS, KRW-REP, KRW-ADA, KRW-SBD, KRW-POWR, KRW-BTG, KRW-ICX, KRW-EOS, KRW-TRX, KRW-SC, KRW-ONT, KRW-ZIL, KRW-POLY, KRW-ZRX, KRW-LOOM, KRW-BCH, KRW-BAT, 'KRW-IOST, KRW-RFR, KRW-CVC, KRW-IQ, KRW-IOTA, KRW-MFT, KRW-ONG, KRW-GAS, KRW-UPP, KRW-ELF, KRW-KNC, KRW-BSV, KRW-THETA, KRW-QKC, KRW-BTT, KRW-MOC, KRW-ENJ, KRW-TFUEL, KRW-MANA, KRW-ANKR, KRW-AERGO, KRW-ATOM, KRW-TT, KRW-CRE, KRW-MBL, KRW-WAXP, KRW-HBAR, KRW-MED, KRW-MLK, KRW-STPT, KRW-ORBS, KRW-VET, KRW-CHZ, KRW-STMX, KRW-DKA, KRW-HIVE, KRW-KAVA, KRW-AHT, KRW-LINK, KRW-XTZ, KRW-BORA, KRW-JST, KRW-CRO, KRW-TON, KRW-SXP, KRW-HUNT, KRW-PLA, KRW-DOT, KRW-SRM, KRW-MVL, KRW-STRAX, KRW-AQT, KRW-GLM, KRW-SSX, KRW-META, KRW-FCT2, KRW-CBK, KRW-SAND, KRW-HUM, KRW-DOGE, KRW-STRK, KRW-PUNDIX, KRW-FLOW, KRW-DAWN, KRW-AXS, KRW-STX, KRW-XEC, KRW-SOL, KRW-MATIC, KRW-NU, KRW-AAVE, KRW-1INCH, KRW-ALGO, KRW-NEAR, KRW-WEMIX, KRW-AVAX, KRW-T, KRW-CELO, KRW-GMT, KRW-APT", btc * 0.9995)
        time.sleep(1)
    except Exception as e:
        print(e)
        time.sleep(1)  