# Import required libraries
from os import curdir
from pandas.core.dtypes.generic import create_pandas_abc_type
import streamlit as st
import pandas as pd
from datetime import datetime
from dataclasses import dataclass
from typing import Any, List
import pandas as pd
import hashlib
from typing import List
from dotenv import load_dotenv
import os
import finnhub

from coinmarketcap_api import get_crypto_tickers#, get_crypto_price

st.markdown("# The Crypto Caller")
st.markdown("*Input Project Description...*")
st.markdown("""### Please input your existing cryptocurrency portfolio below:""")

@st.cache(allow_output_mutation=True)
def user_portfolio():
    return []

####################################################### Looking for a solution here for displaySymbol()
cryptocurrency = st.selectbox("Select a Cryptocurrency", get_crypto_tickers())
# quote = get_crypto_price()

amount = st.number_input("Quantity of Coin/Token")

#crypto_usd = get_crypto_prices(cryptocurrency)

if st.button("Add Portfolio Position"):
    user_portfolio().append({"Ticker": cryptocurrency, "Amount": amount})

if st.button("Delete Portfolio Position"):
    user_portfolio().remove({"Ticker":cryptocurrency, "Amount":amount})

user_portfolio_df = pd.DataFrame(user_portfolio())

st.write(user_portfolio_df)

