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

st.markdown("# The Crypto Caller")
st.markdown("*Input Project Description...*")
st.markdown("""### Please input your existing cryptocurrency portfolio below:""")

@st.cache(allow_output_mutation=True)
def user_portfolio():
    return []

cryptocurrency = st.selectbox("Select a Cryptocurrency", ('BTC', 'ETH', 'BNB', 'USDT', 'SOL', 'ADA', 'XRP', 'DOT', 'USDC', 'DOGE', 'SHIB', 'AVAX', 'LUNA', 'LTC', 'WBTC', 'LINK', 'UNI', 'BUSD', 'CRO', 'BCH', 'MATIC', 'ALGO', 'VET', 'AXS', 'XLM', 'TRX', 'ICP', 'FIL', 'ETC', 'DAI', 'THETA', 'ATOM', 'BTCB', 'HBAR', 'FTT', 'UST', 'EGLD', 'MANA', 'FTM', 'NEAR', 'HNT', 'XTZ', 'GRT', 'XMR', 'EOS', 'MIOTA', 'CAKE', 'FLOW', 'KLAY', 'AAVE', 'LRC', 'XEC', 'KDA', 'KSM', 'BSV', 'NEO', 'SAND', 'LEO', 'QNT', 'CHZ', 'RUNE', 'STX', 'MKR', 'ONE', 'ENJ', 'BTT', 'AMP', 'WAVES', 'HOT', 'ZEC', 'DASH', 'AR', 'IOTX', 'COMP', 'KCS', 'NEXO', 'CELO', 'TFUEL', 'XEM', 'HT', 'CRV', 'BAT', 'WAXP', 'OKB', 'ICX', 'QTUM', 'DCR', 'OMG', 'MINA', 'SUSHI', 'TUSD', 'LPT', 'REV', 'UMA', 'RVN', 'SCRT', 'ZIL', 'YFI', 'AUDIO', 'BTG', 'ANKR', 'XDC', 'PERP', 'IMX', 'TEL', 'SNX', 'CEL', 'RENBTC', 'ZEN', 'BORA', 'SC', 'BNT', 'ELON', 'ZRX', 'USDP', 'ONT', 'VLX', 'WOO', 'VGX', 'IOST', 'SRM', 'MOVR', 'RAY', 'NANO', 'DGB', 'REN', 'SKL', 'CHSB', 'DYDX', 'CKB', 'XYO', '1INCH', 'CELR', 'WIN', 'NU', 'DENT', 'GNO', 'TRAC', 'MDX', 'GLM', 'STORJ', 'FET', 'XDB', 'USDN', 'POLY', 'KAVA', 'OCEAN', 'INJ', 'RSR', 'SXP', 'CHR', 'GT', 'REEF', 'CTSI', 'XVG', 'ALPHA', 'LSK', 'MED', 'FX', 'CEEK', 'WRX', 'FLUX', 'FEI', 'NKN', 'NMR', 'HIVE', 'COTI', 'OXT', 'VTHO', 'BTCST', 'CSPR', 'BAKE', 'ARDR', 'BCD', 'CVC', 'UOS', 'OGN', 'RLC', 'SNT', 'ONG', 'PAXG', 'CFX', 'ALICE', 'STMX', 'ELF', 'ROSE', 'POWR', 'STRAX', 'ASD', 'UBT', 'ORBS', 'BADGER', 'KP3R', 'ERG', 'EWT', 'TOMO', 'VRA', 'SYS', 'PROM', 'BAND'))
amount = st.number_input("Quantity of Coin/Token")

if st.button("Add Portfolio Position"):
    user_portfolio().append({"Ticker": cryptocurrency, "Amount": amount})

if st.button("Delete Portfolio Position"):
    user_portfolio().remove({"Ticker": cryptocurrency, "Amount":amount})

user_portfolio_df = pd.DataFrame(user_portfolio())

st.write(user_portfolio_df)

