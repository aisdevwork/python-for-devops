import requests
import json
"""Finding Market Data by EOD from API using python"""

API_KEY = "5d2f97b584e5a6fd303fc2bfd79d95fa"
# symbols = "AAPL" 

# market_url = "https://api.marketstack.com/v1/eod?access_key={API_KEY}&symbols={symbols}"

api_url = "https://api.marketstack.com/v1/eod"  # Base url



def market_EOD(symbols):
    query = f"?access_key={API_KEY}&symbols={symbols}" # Query url
    mkt_url = api_url + query
    response = requests.get(mkt_url)
    meta = response.json()
    #print(f"\n{meta['data'][0]['symbol']}") 
    store_data = []
    n = len(meta["data"])
    for i in range(0,n): 
        stock = meta["data"][i]
        print(f""" 
            Symbol  :{stock['symbol']}
            Date    :{stock['date']}
            Exchange:{stock['exchange']}
            High    :{stock['high']}
            Low     :{stock['low']}
            Open    :{stock['open']}
            Close   :{stock['close']}
                """)
        item = {
            "symbol": stock["symbol"],
            "date": stock["date"],
            "exchange": stock["exchange"],
            "high": stock["high"],
            "low": stock["low"],
            "open": stock["open"],
            "close": stock["close"]
                }
        store_data.append(item)
    return store_data  


symbols = input("Enter the Stockname(Eg: AAPL, MSFT ,NKE):")
data = market_EOD(symbols)

with open("output.json","w") as file:
    json.dump(data, file, indent=4)   