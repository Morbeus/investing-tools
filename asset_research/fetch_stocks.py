# We will use the nselib API for getting the list of equities. 
# once we have a list of equities we will use the yahoo finance api for getting the required stock data
import yfinance as yf
import pandas as pd

# Fetching data for RELIANCE.NS
ticker = 'RELIANCE.NS'
stock = yf.Ticker(ticker)
info = stock.info

# Converting the JSON object to a DataFrame
df = pd.DataFrame([info])
print(df.head())
# Saving the DataFrame to a CSV file
df.to_csv('reliance_info.csv', index=False)

print("Data saved to reliance_info.csv")

    # # Extracting required data
    # company_name = info.get('longName', 'N/A')
    # market_cap = info.get('marketCap', 'N/A')
    # pe_ratio = info.get('trailingPE', 'N/A')
    # forward_pe_ratio = info.get('forwardPE', 'N/A')
    # price_to_book = info.get('priceToBook', 'N/A')
    # dividend_yield = info.get('dividendYield', 'N/A')
    # beta = info.get('beta', 'N/A')
    # eps = info.get('trailingEps', 'N/A')
    
    # # Displaying the data
    # print(f"--- {company_name} ({ticker}) ---")
    # print(f"Market Cap: {market_cap}")
    # print(f"P/E Ratio: {pe_ratio}")
    # print(f"Forward P/E Ratio: {forward_pe_ratio}")
    # print(f"Price to Book Ratio: {price_to_book}")
    # print(f"Dividend Yield: {dividend_yield}")
    # print(f"Beta: {beta}")
    # print(f"EPS: {eps}")

