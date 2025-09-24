import numpy as np
import pandas as pd
from scipy.stats import norm
import yfinance as yf

#Gathering User Information
ticker = input("Please Input Stock Ticker: ")
stockPrice = float(input("Please Input Stock Price: "))
strikePrice = float(input("Please Input Strike Price: "))
riskFreeRate = float(input("Please Input Risk Free Rate (Annual): "))
time = float(input("Please Input Time of Expiration (Years): "))

#Gathering Data from Yahoo Finance
data = yf.download(ticker, start="2024-09-18", end="2025-09-18")
data.columns = ["Close", "High", "Low", "Open", "Volume"] #reformatting

#Computing Annualized Logarithmic Standard Deviation
data["LogReturns"] = np.log(data["Close"]/data["Close"].shift(1))
data = data[1:]
std = data["LogReturns"].std()*(255**0.5)

#D1
D1 = ((np.log(stockPrice/strikePrice) + (riskFreeRate+0.5*std**2)*time)) / (std * np.sqrt(time))

#D2
D2 = D1 - std*np.sqrt(time)

#Computation
optionPrice = stockPrice * norm.cdf(D1) - strikePrice * np.exp(-riskFreeRate*time) * norm.cdf(D2)

#Returning Results
print("Option Call Price: ", optionPrice)
