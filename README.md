# CCXT – CryptoCurrency eXchange Trading Library

[![Build Status](https://travis-ci.org/ccxt/ccxt.svg?branch=master)](https://travis-ci.org/ccxt/ccxt) [![npm](https://img.shields.io/npm/v/ccxt.svg)](https://npmjs.com/package/ccxt) [![PyPI](https://img.shields.io/pypi/v/ccxt.svg)](https://pypi.python.org/pypi/ccxt) [![NPM Downloads](https://img.shields.io/npm/dm/ccxt.svg)](https://www.npmjs.com/package/ccxt) [![Gitter](https://badges.gitter.im/ccxt-dev/ccxt.svg)](https://gitter.im/ccxt-dev/ccxt?utm_source=badge&utm_medium=badge&utm_campaign=pr-badge) [![Supported Exchanges](https://img.shields.io/badge/exchanges-134-blue.svg)](https://github.com/ccxt/ccxt/wiki/Exchange-Markets) [![Open Collective](https://opencollective.com/ccxt/backers/badge.svg)](https://opencollective.com/ccxt)
[![Twitter Follow](https://img.shields.io/twitter/follow/ccxt_official.svg?style=social&label=CCXT)](https://twitter.com/ccxt_official)

A JavaScript / Python / PHP library for cryptocurrency trading and e-commerce with support for many bitcoin/ether/altcoin exchange markets and merchant APIs.

### [Install](#install) · [Usage](#usage) · [Manual](https://github.com/ccxt/ccxt/wiki) · [FAQ](https://github.com/ccxt/ccxt/wiki/FAQ) · [Examples](https://github.com/ccxt/ccxt/tree/master/examples) · [Contributing](https://github.com/ccxt/ccxt/blob/master/CONTRIBUTING.md) · [Social](#social)

The **CCXT** library is used to connect and trade with cryptocurrency exchanges and payment processing services worldwide. It provides quick access to market data for storage, analysis, visualization, indicator development, algorithmic trading, strategy backtesting, bot programming, and related software engineering.

It is intended to be used by **coders, developers, technically-skilled traders, data-scientists and financial analysts** for building trading algorithms.

Current feature list:

- support for many cryptocurrency exchanges — more coming soon
- fully implemented public and private APIs
- optional normalized data for cross-exchange analytics and arbitrage
- an out of the box unified API that is extremely easy to integrate
- works in Node 7.6+, Python 2 and 3, PHP 5.4+, and web browsers

## Sponsored Promotion

[![https://www.coss.io](https://user-images.githubusercontent.com/1294454/49981835-f497b780-ff6a-11e8-8377-03c31cb8e402.gif)](https://www.coss.io)

## Certified Cryptocurrency Exchanges

                                 |
|[![zb](https://user-images.githubusercontent.com/1294454/32859187-cd5214f0-ca5e-11e7-967d-96568e2e2bd1.jpg)](https://vip.zb.com/user/register?recommendCode=bn070u)                          | zb                 | [ZB](https://vip.zb.com/user/register?recommendCode=bn070u)                          | 1     | [API](https://www.zb.com/i/developer)                                                            |                                                                                                                             | China                                   |

The list above is updated frequently, new crypto markets, exchanges, bug fixes, and API endpoints are introduced on a regular basis. See the [Manual](https://github.com/ccxt/ccxt/wiki) for more details. If you can't find a cryptocurrency exchange in the list above and want it to be added, post a link to it by opening an issue here on GitHub or send us an email.

The library is under [MIT license](https://github.com/ccxt/ccxt/blob/master/LICENSE.txt), that means it's absolutely free for any developer to build commercial and opensource software on top of it, but use it at your own risk with no warranties, as is.

---

## Documentation

Read the [Manual](https://github.com/ccxt/ccxt/wiki) for more details.

## Usage

### Intro

The CCXT library consists of a public part and a private part. Anyone can use the public part immediately after installation. Public APIs provide unrestricted access to public information for all exchange markets without the need to register a user account or have an API key.

Public APIs include the following:

- market data
- instruments/trading pairs
- price feeds (exchange rates)
- order books
- trade history
- tickers
- OHLC(V) for charting
- other public endpoints

In order to trade with private APIs you need to obtain API keys from an exchange's website. It usually means signing up to the exchange and creating API keys for your account. Some exchanges require personal info or identification. Sometimes verification may be necessary as well. In this case you will need to register yourself, this library will not create accounts or API keys for you. Some exchanges expose API endpoints for registering an account, but most exchanges don't. You will have to sign up and create API keys on their websites.

Private APIs allow the following:

- manage personal account info
- query account balances
- trade by making market and limit orders
- deposit and withdraw fiat and crypto funds
- query personal orders
- get ledger history
- transfer funds between accounts
- use merchant services

This library implements full public and private REST APIs for all exchanges. WebSocket and FIX implementations in JavaScript, PHP, Python and other languages coming soon.

The CCXT library supports both camelcase notation (preferred in JavaScript) and underscore notation (preferred in Python and PHP), therefore all methods can be called in either notation or coding style in any language.

```JavaScript
// both of these notations work in JavaScript/Python/PHP
exchange.methodName ()  // camelcase pseudocode
exchange.method_name () // underscore pseudocode
```

Read the [Manual](https://github.com/ccxt/ccxt/wiki) for more details.

### JavaScript

```JavaScript
'use strict';
const ccxt = require ('ccxt');

(async function () {
    let kraken    = new ccxt.kraken ()
    let bitfinex  = new ccxt.bitfinex ({ verbose: true })
    let huobi     = new ccxt.huobi ()
    let okcoinusd = new ccxt.okcoinusd ({
        apiKey: 'YOUR_PUBLIC_API_KEY',
        secret: 'YOUR_SECRET_PRIVATE_KEY',
    })

    const exchangeId = 'binance'
        , exchangeClass = ccxt[exchangeId]
        , exchange = new exchangeClass ({
            'apiKey': 'YOUR_API_KEY',
            'secret': 'YOUR_SECRET',
            'timeout': 30000,
            'enableRateLimit': true,
        })

    console.log (kraken.id,    await kraken.loadMarkets ())
    console.log (bitfinex.id,  await bitfinex.loadMarkets  ())
    console.log (huobi.id,     await huobi.loadMarkets ())

    console.log (kraken.id,    await kraken.fetchOrderBook (kraken.symbols[0]))
    console.log (bitfinex.id,  await bitfinex.fetchTicker ('BTC/USD'))
    console.log (huobi.id,     await huobi.fetchTrades ('ETH/CNY'))

    console.log (okcoinusd.id, await okcoinusd.fetchBalance ())

    // sell 1 BTC/USD for market price, sell a bitcoin for dollars immediately
    console.log (okcoinusd.id, await okcoinusd.createMarketSellOrder ('BTC/USD', 1))

    // buy 1 BTC/USD for $2500, you pay $2500 and receive ฿1 when the order is closed
    console.log (okcoinusd.id, await okcoinusd.createLimitBuyOrder ('BTC/USD', 1, 2500.00))

    // pass/redefine custom exchange-specific order params: type, amount, price or whatever
    // use a custom order type
    bitfinex.createLimitSellOrder ('BTC/USD', 1, 10, { 'type': 'trailing-stop' })

}) ();
```

### Python

```Python
# coding=utf-8

import ccxt

hitbtc = ccxt.hitbtc({'verbose': True})
bitmex = ccxt.bitmex()
huobi  = ccxt.huobi()
exmo   = ccxt.exmo({
    'apiKey': 'YOUR_PUBLIC_API_KEY',
    'secret': 'YOUR_SECRET_PRIVATE_KEY',
})
kraken = ccxt.kraken({
    'apiKey': 'YOUR_PUBLIC_API_KEY',
    'secret': 'YOUR_SECRET_PRIVATE_KEY',
})

exchange_id = 'binance'
exchange_class = getattr(ccxt, exchange_id)
exchange = exchange_class({
    'apiKey': 'YOUR_API_KEY',
    'secret': 'YOUR_SECRET',
    'timeout': 30000,
    'enableRateLimit': True,
})

hitbtc_markets = hitbtc.load_markets()

print(hitbtc.id, hitbtc_markets)
print(bitmex.id, bitmex.load_markets())
print(huobi.id, huobi.load_markets())

print(hitbtc.fetch_order_book(hitbtc.symbols[0]))
print(bitmex.fetch_ticker('BTC/USD'))
print(huobi.fetch_trades('LTC/CNY'))

print(exmo.fetch_balance())

# sell one ฿ for market price and receive $ right now
print(exmo.id, exmo.create_market_sell_order('BTC/USD', 1))

# limit buy BTC/EUR, you pay €2500 and receive ฿1  when the order is closed
print(exmo.id, exmo.create_limit_buy_order('BTC/EUR', 1, 2500.00))

# pass/redefine custom exchange-specific order params: type, amount, price, flags, etc...
kraken.create_market_buy_order('BTC/USD', 1, {'trading_agreement': 'agree'})
```

### PHP

```PHP
include 'ccxt.php';

$poloniex = new \ccxt\poloniex ();
$bittrex  = new \ccxt\bittrex  (array ('verbose' => true));
$quoinex  = new \ccxt\quoinex   ();
$zaif     = new \ccxt\zaif     (array (
    'apiKey' => 'YOUR_PUBLIC_API_KEY',
    'secret' => 'YOUR_SECRET_PRIVATE_KEY',
));
$hitbtc   = new \ccxt\hitbtc   (array (
    'apiKey' => 'YOUR_PUBLIC_API_KEY',
    'secret' => 'YOUR_SECRET_PRIVATE_KEY',
));

$exchange_id = 'binance';
$exchange_class = "\\ccxt\\$exchange_id";
$exchange = new $exchange_class (array (
    'apiKey' => 'YOUR_API_KEY',
    'secret' => 'YOUR_SECRET',
    'timeout' => 30000,
    'enableRateLimit' => true,
));

$poloniex_markets = $poloniex->load_markets ();

var_dump ($poloniex_markets);
var_dump ($bittrex->load_markets ());
var_dump ($quoinex->load_markets ());

var_dump ($poloniex->fetch_order_book ($poloniex->symbols[0]));
var_dump ($bittrex->fetch_trades ('BTC/USD'));
var_dump ($quoinex->fetch_ticker ('ETH/EUR'));
var_dump ($zaif->fetch_ticker ('BTC/JPY'));

var_dump ($zaif->fetch_balance ());

// sell 1 BTC/JPY for market price, you pay ¥ and receive ฿ immediately
var_dump ($zaif->id, $zaif->create_market_sell_order ('BTC/JPY', 1));

// buy BTC/JPY, you receive ฿1 for ¥285000 when the order closes
var_dump ($zaif->id, $zaif->create_limit_buy_order ('BTC/JPY', 1, 285000));

// set a custom user-defined id to your order
$hitbtc->create_order ('BTC/USD', 'limit', 'buy', 1, 3000, array ('clientOrderId' => '123'));
```

## Contributing

Please read the [CONTRIBUTING](https://github.com/ccxt/ccxt/blob/master/CONTRIBUTING.md) document before making changes that you would like adopted in the code. Also, read the [Manual](https://github.com/ccxt/ccxt/wiki) for more details.

## Support Developer Team

We are investing a significant amount of time into the development of this library. If CCXT made your life easier and you want to help us improve it further, or if you want to speed up development of new features and exchanges, please support us with a tip. We appreciate all contributions!

### Sponsors

Support this project by becoming a sponsor. Your logo will show up here with a link to your website.

[[Become a sponsor](https://opencollective.com/ccxt#sponsor)]

<a href="https://opencollective.com/ccxt/tiers/sponsor/0/website" target="_blank"><img src="https://opencollective.com/ccxt/tiers/sponsor/0/avatar.svg"></a>
<a href="https://opencollective.com/ccxt/tiers/sponsor/1/website" target="_blank"><img src="https://opencollective.com/ccxt/tiers/sponsor/1/avatar.svg"></a>
<a href="https://opencollective.com/ccxt/tiers/sponsor/2/website" target="_blank"><img src="https://opencollective.com/ccxt/tiers/sponsor/2/avatar.svg"></a>
<a href="https://opencollective.com/ccxt/tiers/sponsor/3/website" target="_blank"><img src="https://opencollective.com/ccxt/tiers/sponsor/3/avatar.svg"></a>
<a href="https://opencollective.com/ccxt/tiers/sponsor/4/website" target="_blank"><img src="https://opencollective.com/ccxt/tiers/sponsor/4/avatar.svg"></a>
<a href="https://opencollective.com/ccxt/tiers/sponsor/5/website" target="_blank"><img src="https://opencollective.com/ccxt/tiers/sponsor/5/avatar.svg"></a>
<a href="https://opencollective.com/ccxt/tiers/sponsor/6/website" target="_blank"><img src="https://opencollective.com/ccxt/tiers/sponsor/6/avatar.svg"></a>
<a href="https://opencollective.com/ccxt/tiers/sponsor/7/website" target="_blank"><img src="https://opencollective.com/ccxt/tiers/sponsor/7/avatar.svg"></a>
<a href="https://opencollective.com/ccxt/tiers/sponsor/8/website" target="_blank"><img src="https://opencollective.com/ccxt/tiers/sponsor/8/avatar.svg"></a>
<a href="https://opencollective.com/ccxt/tiers/sponsor/9/website" target="_blank"><img src="https://opencollective.com/ccxt/tiers/sponsor/9/avatar.svg"></a>

### Supporters

Support this project by becoming a supporter. Your avatar will show up here with a link to your website.

[[Become a supporter](https://opencollective.com/ccxt#supporter)]

<a href="https://opencollective.com/ccxt/tiers/supporter/0/website" target="_blank"><img src="https://opencollective.com/ccxt/tiers/supporter/0/avatar.svg"></a>
<a href="https://opencollective.com/ccxt/tiers/supporter/1/website" target="_blank"><img src="https://opencollective.com/ccxt/tiers/supporter/1/avatar.svg"></a>
<a href="https://opencollective.com/ccxt/tiers/supporter/2/website" target="_blank"><img src="https://opencollective.com/ccxt/tiers/supporter/2/avatar.svg"></a>
<a href="https://opencollective.com/ccxt/tiers/supporter/3/website" target="_blank"><img src="https://opencollective.com/ccxt/tiers/supporter/3/avatar.svg"></a>
<a href="https://opencollective.com/ccxt/tiers/supporter/4/website" target="_blank"><img src="https://opencollective.com/ccxt/tiers/supporter/4/avatar.svg"></a>
<a href="https://opencollective.com/ccxt/tiers/supporter/5/website" target="_blank"><img src="https://opencollective.com/ccxt/tiers/supporter/5/avatar.svg"></a>
<a href="https://opencollective.com/ccxt/tiers/supporter/6/website" target="_blank"><img src="https://opencollective.com/ccxt/tiers/supporter/6/avatar.svg"></a>
<a href="https://opencollective.com/ccxt/tiers/supporter/7/website" target="_blank"><img src="https://opencollective.com/ccxt/tiers/supporter/7/avatar.svg"></a>
<a href="https://opencollective.com/ccxt/tiers/supporter/8/website" target="_blank"><img src="https://opencollective.com/ccxt/tiers/supporter/8/avatar.svg"></a>
<a href="https://opencollective.com/ccxt/tiers/supporter/9/website" target="_blank"><img src="https://opencollective.com/ccxt/tiers/supporter/9/avatar.svg"></a>

### Backers

Thank you to all our backers! [[Become a backer](https://opencollective.com/ccxt#backer)]

<a href="https://opencollective.com/ccxt#backers" target="_blank"><img src="https://opencollective.com/ccxt/tiers/backer.svg?width=890"></a>

### Crypto

```
ETH 0x26a3CB49578F07000575405a57888681249c35Fd (ETH only)
BTC 33RmVRfhK2WZVQR1R83h2e9yXoqRNDvJva
BCH 1GN9p233TvNcNQFthCgfiHUnj5JRKEc2Ze
LTC LbT8mkAqQBphc4yxLXEDgYDfEax74et3bP
```

Thank you!

## Social

- [Follow us on Twitter](https://twitter.com/ccxt_official)
- [Read our blog on Medium](https://medium.com/@ccxt)

## Team

- [Igor Kroitor](https://github.com/kroitor)
- [Vitaly Gordon](https://github.com/xpl)
- [Denis Voropaev](https://github.com/tankakatan)
- [Carlo Revelli](https://github.com/frosty00)

## Contact Us

For business inquiries: info@ccxt.trade
