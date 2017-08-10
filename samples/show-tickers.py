#!/usr/bin/env python
import tidexapi

attrs = ('high', 'low', 'avg', 'vol', 'vol_cur', 'last',
         'buy', 'sell', 'updated')

print("Tickers:")
connection = tidexapi.Connection()
info = tidexapi.APIInfo(connection)
for pair in info.pair_names:
    ticker = tidexapi.getTicker(pair, connection)
    print(pair)
    for a in attrs:
        print("\t%s %s" % (a, getattr(ticker, a)))
