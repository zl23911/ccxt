import time
import pandas as pd
import ccxt

if __name__ == '__main__':
    zbg = ccxt.zbg()
    zbg.apiKey = '7ljSc36ADq47ljSc36ADq5'
    zbg.secret = '7d939853803e90978fb3e52be744d19d'
    # print(zbg.fetch_markets())

    # print(zbg.fetch_balance())

    # print(zbg.fetch_ticker(symbol='btc/usdt'))

    # print(zbg.fetch_trades(symbol='btc/usdt'))

    # print(zbg.fetch_order_book(symbol='btc/usdt'))

    # print(zbg.fetch_ohlcv(symbol='btc/usdt', timeframe='1h'))

    # print(zbg.fetch_order(id='E6518698817490001920', symbol='ZT/USDT'))

    print(zbg.fetch_orders(symbol='ZT/USDT', since=1548415379921))

    # add_result = zbg.create_order("ZT/USDT", '', 'buy', 100, 1.2)
    # print(add_result)
    # time.sleep(1)
    # print(zbg.cancel_order(add_result['id'], "ZT/USDT"))

    # print(zbg.cancel_order('E6521346130393964544', "ZT/USDT"))


    # 请求的candles个数
    limit = 500

    #  当前时间
    current_time = int(time.time() // 60 * 60 * 1000)  # 毫秒
    print(current_time)

    # 获取请求开始的时间
    since_time = current_time - limit * 60 * 1000

    #  'BTC/USD' 比特币对美元的交易对，或者ETH/USD 以太坊对美元的交易对.
    data = zbg.fetch_ohlcv(symbol='BTC/USDT', limit=500, since=None)
    print(data)
    df = pd.DataFrame(data)
    df = df.rename(columns={0: 'open_time', 1: 'open', 2: 'high', 3: 'low', 4: 'close', 5: 'volume'})

    # 时间转换成北京时间
    df['open_time'] = pd.to_datetime(df['open_time'], unit='ms') + pd.Timedelta(hours=8)

    # 设置index
    df = df.set_index('open_time', drop=True)

    # 保存成csv文件
    df.to_csv('bitmex_data.csv')  # comma seperate Value
    print(df)
