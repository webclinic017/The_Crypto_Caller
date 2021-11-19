import pandas as pd
# from dotenv import load_dotenv
import os
# import finnhub
from requests import Request, Session
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects
import json

listing_url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest'
headers = {
  'Accepts': 'application/json',
  'X-CMC_PRO_API_KEY': '16309f60-d6b0-492a-8596-06df4758b8c2',
}
session = Session()
session.headers.update(headers)













# pulling crypto pairs from Finnhub
def displaySymbol():
    symbol = pd.DataFrame(
        finnhub_client.crypto_symbols("COINBASE")
    )
    symbol = symbol["symbol"]
    return symbol

displaySymbol()

if __name__ == '__main__':
    running=True
