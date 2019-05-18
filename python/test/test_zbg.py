import time
import unittest
import ccxt


class TestZbg(unittest.TestCase):
    test_market_name = 'ADA/USDT'
    test_market_id = '80'
    test_currency_name = 'BTC'
    zbg = ccxt.zbg()
    zbg.apiKey = ''
    zbg.secret = ''

    # def test_create_order(self):
    #     result = self.zbg.create_order(self.test_market_name, '', 'buy', 1, 0.6)
    #
    #     print('\n' + 'test_create_order:')
    #     print(result)
    #
    #     assert result['id'] is not None

    # def test_cancel_order(self):
    #     time.sleep(1)
    #     result = self.zbg.create_order(self.test_market_name, '', 'buy', 1, 0.6)
    #
    #     time.sleep(1)
    #     result = self.zbg.cancel_order(result['id'], self.test_market_name)
    #
    #     print('\n' + 'test_cancel_order:')
    #     print(result)
    #
    # def test_cancel_orders(self):
    #     time.sleep(1)
    #     result = self.zbg.create_order(self.test_market_name, '', 'buy', 1, 0.6)
    #     time.sleep(1)
    #     result2 = self.zbg.create_order(self.test_market_name, '', 'sell', 1, 0.7)
    #     time.sleep(1)
    #     result3 = self.zbg.create_order(self.test_market_name, '', 'buy', 1, 0.5)
    #
    #     time.sleep(1)
    #     result = self.zbg.cancel_orders(self.test_market_name, result['id'], result2['id'], result3['id'])
    #
    #     print('\n' + 'test_cancel_orders:')
    #     print(result)
    #
    # def test_fetch_markets(self):
    #     result = self.zbg.fetch_markets()
    #
    #     print('\n' + 'test_fetch_markets:')
    #     print(result)
    #
    # def test_fetch_balance(self):
    #     result = self.zbg.fetch_balance(self.test_market_name)
    #
    #     print('\n' + 'test_fetch_balance:')
    #     print(result)
    #
    # def test_fetch_order(self):
    #     time.sleep(1)
    #     result = self.zbg.create_order(self.test_market_name, '', 'buy', 1, 0.6)
    #
    #     time.sleep(1)
    #
    #     result = self.zbg.fetch_order(result['id'], self.test_market_name)
    #
    #     print('\n' + 'test_fetch_order:')
    #     print(result)

    # def test_fetch_orders(self):
    #     result = self.zbg.fetch_orders(self.test_market_name, limit=2)
    #
    #     print('\n' + 'test_fetch_orders:')
    #     print(result)
    #
    #     result = self.zbg.fetch_orders(self.test_market_name, limit=2, params={'pageIndex': 2})
    #
    #     print('\n' + 'test_fetch_orders page 2:')
    #     print(result)

    def test_fetch_open_orders(self):
        result = self.zbg.fetch_open_orders(self.test_market_name, limit=2)

        print('\n' + 'fetch_open_orders:')
        print(result)

        result = self.zbg.fetch_open_orders(self.test_market_name, limit=2, params={'pageIndex': 1})

        print('\n' + 'fetch_open_orders page 2:')
        print(result)

    # def test_fetch_trades(self):
    #     result = self.zbg.fetch_trades(self.test_market_name, limit=20)
    #
    #     print('\n' + 'test_fetch_trades:')
    #     print(result)
    #
    # def test_fetch_transactions(self):
    #     result = self.zbg.fetch_transactions(self.test_market_name, limit=20)
    #
    #     print('\n' + 'test_fetch_transactions:')
    #     print(result)


if __name__ == '__main__':
    unittest.main()
