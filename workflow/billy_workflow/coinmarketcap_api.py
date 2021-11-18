from requests import Request, Session
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects
import json
import pandas as pd



headers = {
  'Accepts': 'application/json',
  'X-CMC_PRO_API_KEY': '16309f60-d6b0-492a-8596-06df4758b8c2',
}
session = Session()
session.headers.update(headers)

def get_crypto_tickers():
    url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest'
    parameters = {
        'start':'1',
        'limit':'1000',
        'convert':'USD'
    }
    response = session.get(url, params=parameters)
    data = json.loads(response.text)
    crypto_symbols = []
    for row in data['data']:
        crypto_symbols.append(pd.Series(row))
    crypto_df = pd.DataFrame(
        data = crypto_symbols
    )
    crypto_df = crypto_df["symbol"]
    return crypto_df

# still working on this function...
def get_crypto_price():
    parameters = {

    }

    response = session.get(url, params=parameters)
    data = json.loads(response.text)
    crypto_quote = []
    for row in data['data']:
        crypto_quote.append(pd.Series(row))
    crypto_quote_df = pd.DataFrame(
        data = crypto_quote
    )
    crypto_quote_df = crypto_quote_df["quote"]
    return crypto_quote_df
