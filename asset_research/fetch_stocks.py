# We will use the nselib API for getting the list of equities. 
# once we have a list of equities we will use the yahoo finance api for getting the required stock data

import yfinance as yf

tickers = ['RELIANCE.NS', 'TCS.NS', 'INFY.NS']
# data = yf.download(tickers, start="2023-01-01", end="2023-08-10")
# print(data)

# Loop through each ticker to get additional data
for ticker in tickers:
    stock = yf.Ticker(ticker)
    
    # Fetching fundamental data
    info = stock.info
    print(info)
    
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

