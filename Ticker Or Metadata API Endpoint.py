import json
from requests import Session
import numpy as np

start = 1
limit = 5
ar = list(np.arange(start, start + limit))
ids = ",".join(str(x) for x in ar)

url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/quotes/latest?id=' + ids

headers = {
    'Accepts': 'application/json',
    'X-CMC_PRO_API_KEY': 'API_KEY',
}

session = Session()
session.headers.update(headers)

response = session.get(url)
results = response.json()

print(json.dumps(results, sort_keys=True, indent=4))

data = results["data"]

for key, currency in data.items():
    rank = currency["cmc_rank"]
    name = currency["name"]
    symbol = currency["symbol"]

    circulating_supply = int(currency["circulating_supply"])
    total_supply = int(currency["total_supply"])

    quotes = currency["quote"]["USD"]
    market_cap = quotes["market_cap"]
    hour_change = quotes["percent_change_1h"]
    day_change = quotes["percent_change_24h"]
    week_change = quotes["percent_change_7d"]

    price = quotes["price"]
    volume = quotes["volume_24h"]

    volume_string = "{:,}".format(volume)
    market_cap_string = "{:,}".format(market_cap)
    circulating_supply_string = "{:,}".format(circulating_supply)
    total_supply_string = "{:,}".format(total_supply)

    print(str(rank) + " : " + name + "( " + symbol + " ) ")
    print('Market Cap :                          $' + market_cap_string)
    print('Price :                               $' + str(price))
    print('24h Volume :                          $' + volume_string)
    print('Hour Change :                          ' + str(hour_change) + '%')
    print('Day Change :                           ' + str(day_change) + '%')
    print('Week Change :                          ' + str(week_change) + '%')

    print("Total Supply :                         " + total_supply_string)
    print("Circulating Supply :                   " + total_supply_string)
    print("Percentage of coins in circulation :   " + str(round(circulating_supply / total_supply)*100) + "%")
    print()
