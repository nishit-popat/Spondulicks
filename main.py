import logging

from connectors.binance_futures import BinanceFuturesClient
from connectors.bitmex import BitmexClient

from interface.root_component import Root
import config


logger = logging.getLogger()

logger.setLevel(logging.INFO)

stream_handler = logging.StreamHandler()
formatter = logging.Formatter('%(asctime)s %(levelname)s :: %(message)s')
stream_handler.setFormatter(formatter)
stream_handler.setLevel(logging.INFO)

file_handler = logging.FileHandler('info.log')
file_handler.setFormatter(formatter)
file_handler.setLevel(logging.DEBUG)

logger.addHandler(stream_handler)
logger.addHandler(file_handler)


if __name__ == '__main__':

    # binance = BinanceFuturesClient("", "", True)
    # bitmex = BitmexClient("", "", True)

    binance = BinanceFuturesClient(config.API_KEY_BINANCE, config.API_SECRET_BINANCE, True)

    bitmex = BitmexClient(config.API_KEY_BITMEX, config.API_SECRET_BITMEX, True)

    root = Root(binance, bitmex)
    root.mainloop()


    # API Key
    # bef1b304a3e72ff9b6cd142ae6a23b36ecba5f7dd65cb38f45948f85db9ee033
    # API Secret
    # 9f02961e2a05608cf6b757dc72d40e48803e92e9d5c072a948982a771d352eec