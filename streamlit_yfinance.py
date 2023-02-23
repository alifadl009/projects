import yfinance as yf
import pandas as pd
import streamlit as st

st.write("""
# Simple stock price app
Shown are the stock price and **closing** price and **volume** of Google
""")

data = yf.Ticker('GOOGL')
df = data.history(period='1d', start='2010-1-1', end='2023-02-22')

st.write("""
## Closing Price 
""")
st.line_chart(df.Close)
st.write("""
## Volume Price
""")
st.line_chart(df.Volume)
