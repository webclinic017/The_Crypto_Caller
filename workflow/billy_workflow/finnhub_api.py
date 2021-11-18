import pandas as pd
from dotenv import load_dotenv
import os
import finnhub

def finnhubAPI():
    load_dotenv()
    finnhub_api_key = os.getenv("FINNHUB_API_KEY")
    if type(finnhub_api_key) == str:
        print('API OK')
    else:
        print('API NOT OK', type(finnhub_api_key))
        print('Check your .env file for the FINNHUB_API_KEY value.')
        print('Sign-up and get an API key at https://finnhub.io/')
    finnhub_client = finnhub.Client(api_key=finnhub_api_key)
    return finnhub_client


# pulling crypto pairs from Finnhub
def displaySymbol(finnhub_client):
    symbol = pd.DataFrame(
        finnhub_client.crypto_symbols("COINBAS")
    )
    return symbol["symbol"]
