# investing-tools
Tools that automate the manual tasks that concern the average investor. Making the process easier and faster.

This repository aims to provide the investor with tools at each of the following steps of their investing journey - 

1) Asset Research - 
    * Stock Screening
    * Stock Ratio Analysis
    * Asset Comparison with other assets and asset classes/market
    * AI feature : Provide a score to the management based on sentiment analysis of past 5 years of management discussion and analysis extracted from the Annual Reports(optionally provide the functionality for current reports too)
    * AI feature : Provide an assessment of company's financial health by analysing the cash flows and other financial statements found in the Annual Report(A key segmentor here would be the ability to detect sneaky accounting practices.)
    * Visualisation of metrics for a given time horizon for a given asset and multiple assets when comparing.
    * AI feature : Provide a summary of around 1-2 pages (1000 words max) of the Annual Report so that the investor does not have to read through the entire thing. Optionally provide them with the ability to summarize either the whole document or parts of it.
    * AI feature : Browse the company's website to collect all the news and press releases by the company and summarise them for the user.

2) Building and Managing a Portfolio of stocks 
    * Run efficient frontier and similar tests to determine the right mix of stocks to select from a list of screened stocks. Alternatively, it can be run on a list of pre-screened stocks to eliminate the ones which have low weights in the efficient frontier.
    * Active Recommendation(AI feature) : Based on the portfolio, investor's risk/return expectations, and other factors like diversification recommend stocks to them to optimize their portfolio.
    * Portfolio Rebalancing
    * Ability to CRUD stocks and assets to portfolio manually. And from List of screened/pre-screened assets and also after the efficient frontier test.

3) Monitor and Review Investments
    * Dashboard containing all the investments and insights of interest to the investor
    * AI feature(not completely AI based) : Create a comprehensive report of your investments
