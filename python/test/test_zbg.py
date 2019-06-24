import time
import unittest
import ccxt


class TestZbg(unittest.TestCase):
    test_market_name = 'ETH/KRW'
    test_market_id = '92'
    test_currency_name = 'BTC'
    zbg = ccxt.zbg()
    zbg.apiKey = '7ljSc36ADq47ljSc36ADq5'
    zbg.secret = '7d939853803e90978fb3e52be744d19d'

    def test_create_order(self):
        result = self.zbg.create_order(self.test_market_name, '', 'buy', 1, 0.6)

        print('\n' + 'test_create_order:')
        print(result)

        assert result['id'] is not None

    def test_cancel_order(self):
        time.sleep(1)
        result = self.zbg.create_order(self.test_market_name, '', 'buy', 1, 0.6)

        time.sleep(1)
        result = self.zbg.cancel_order(result['id'], self.test_market_name)

        print('\n' + 'test_cancel_order:')
        print(result)

    def test_cancel_orders(self):
        time.sleep(1)
        result = self.zbg.create_order(self.test_market_name, '', 'buy', 1, 0.6)
        time.sleep(1)
        result2 = self.zbg.create_order(self.test_market_name, '', 'sell', 1, 0.7)
        time.sleep(1)
        result3 = self.zbg.create_order(self.test_market_name, '', 'buy', 1, 0.5)

        time.sleep(1)
        result = self.zbg.cancel_orders(self.test_market_name, result['id'], result2['id'], result3['id'])

        print('\n' + 'test_cancel_orders:')
        print(result)

    def test_fetch_markets(self):
        result = self.zbg.fetch_markets()

        print('\n' + 'test_fetch_markets:')
        print(result)

    def test_fetch_balance(self):
        result = self.zbg.fetch_balance(self.test_market_name)

        print('\n' + 'test_fetch_balance:')
        print(result)

    def test_fetch_order(self):
        time.sleep(1)
        result = self.zbg.create_order(self.test_market_name, '', 'buy', 1, 0.6)

        time.sleep(1)

        result = self.zbg.fetch_order(result['id'], self.test_market_name)

        print('\n' + 'test_fetch_order:')
        print(result)

    def test_fetch_orders(self):
        result = self.zbg.fetch_orders(self.test_market_name, limit=2)

        print('\n' + 'test_fetch_orders:')
        print(result)

        result = self.zbg.fetch_orders(self.test_market_name, limit=2, params={'pageIndex': 2})

        print('\n' + 'test_fetch_orders page 2:')
        print(result)

    def test_fetch_open_orders(self):
        result = self.zbg.fetch_open_orders(self.test_market_name)

        print('\n' + 'fetch_open_orders:')
        print(result)

        result = self.zbg.fetch_open_orders(self.test_market_name, limit=2, params={'pageIndex': 1})

        print('\n' + 'fetch_open_orders page 2:')
        print(result)

    def test_fetch_trades(self):
        result = self.zbg.fetch_trades(self.test_market_name, limit=20)

        print('\n' + 'test_fetch_trades:')
        print(result)

    def test_fetch_my_trades(self):
        result = self.zbg.fetch_my_trades(self.test_market_name, limit=20)

        print('\n' + 'test_fetch_my_trades:')
        print(result)

    def test_fetch_ticker(self):
        result = self.zbg.fetch_ticker(self.test_market_name)

        print('\n' + 'test_fetch_ticker:')
        print(result)

    def test_fetch_tickers(self):
        result = self.zbg.fetch_tickers()

        print('\n' + 'test_fetch_tickers:')
        print(result)

    def test_fetch_order_book(self):
        result = self.zbg.fetch_order_book(self.test_market_name)

        print('\n' + 'test_fetch_order_book:')
        print(result)

    def test_fetch_deposit_address(self):
        result = self.zbg.fetch_deposit_address('EOS')

        print('\n' + 'test_fetch_deposit_address:')
        print(result)

    def test_fetch_deposits(self):
        result = self.zbg.fetch_deposits('ZT', limit=1, params={'pageNum': 2})

        print('\n' + 'test_fetch_deposits:')
        print(result)

    def test_fetch_withdraw_address(self):
        result = self.zbg.fetch_withdraw_address('QC')

        print('\n' + 'test_fetch_withdraw_address:')
        print(result)

    def test_fetch_withdrawals(self):
        result = self.zbg.fetch_withdrawals('QC', limit=1, params={'pageNum': 1})

        print('\n' + 'test_fetch_withdrawals:')
        print(result)

    def test_withdraw(self):
        result = self.zbg.withdraw('QC', 100, '1DkwrD4bMtjd6kcZw8CxM9r3z4AGVFfSRz')

        print('\n' + 'test_withdraw:')
        print(result)

    def test_cancel_withdraw(self):
        result = self.zbg.cancel_withdraw("W6548806224505630720")

        print('\n' + 'test_cancel_withdraw:')
        print(result)


if __name__ == '__main__':
    # unittest.main()
    suite = unittest.TestSuite()
    suite.addTest(TestZbg('test_cancel_withdraw'))

    runner = unittest.TextTestRunner()
    runner.run(suite)
