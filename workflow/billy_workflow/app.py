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

from finnhub_api import displaySymbol

st.markdown("# The Crypto Caller")
st.markdown("*Input Project Description...*")
st.markdown("""### Please input your existing cryptocurrency portfolio below:""")

@st.cache(allow_output_mutation=True)
def user_portfolio():
    return []

cryptocurrency = st.selectbox(
    "Select a Cryptocurrency", 
    displaySymbol()
    )
amount = st.number_input("Quantity of Coin/Token")

if st.button("Add Portfolio Position"):
    user_portfolio().append({"Ticker": cryptocurrency, "Amount": amount})

if st.button("Delete Portfolio Position"):
    user_portfolio().remove({"Ticker": cryptocurrency, "Amount":amount})

user_portfolio_df = pd.DataFrame(user_portfolio())

st.write(user_portfolio_df)

