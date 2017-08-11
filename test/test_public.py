import unittest
from time import sleep

import tidexapi


class TestPublic(unittest.TestCase):
    def test_getTicker(self):
        connection = tidexapi.Connection()
        info = tidexapi.APIInfo(connection)
        for pair in info.pair_names:
            tidexapi.getTicker(pair, connection, info)
            tidexapi.getTicker(pair, connection)
            tidexapi.getTicker(pair, info=info)
            tidexapi.getTicker(pair)

    def test_getHistory(self):
        connection = tidexapi.Connection()
        info = tidexapi.APIInfo(connection)
        for pair in info.pair_names:
            tidexapi.getTradeHistory(pair, connection, info)
            tidexapi.getTradeHistory(pair, connection)
            tidexapi.getTradeHistory(pair, info=info)
            tidexapi.getTradeHistory(pair)

    def test_getDepth(self):
        connection = tidexapi.Connection()
        info = tidexapi.APIInfo(connection)
        for pair in info.pair_names:
            tidexapi.getDepth(pair, connection, info)
            sleep(0.21)
            tidexapi.getDepth(pair, connection)
            sleep(0.21)
            tidexapi.getDepth(pair, info=info)
            sleep(0.21)
            tidexapi.getDepth(pair)
            sleep(0.21)


if __name__ == '__main__':
    unittest.main()
