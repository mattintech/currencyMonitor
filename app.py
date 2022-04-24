from currencyApi import *
from urllib.parse import urlencode
from urllib.request import Request, urlopen
import json

usdAmountToCovert=80000

usdtocad = float(getUsdToCad()) * usdAmountToCovert

print(usdtocad)
url = 'https://api.prowlapp.com/publicapi/add'
post_data = {
    "apikey" : "bd73fe6ae752ef353a068d39346896dccda415e9",
    "priority" : "0",
    "application" : "Currency Watcher",
    "event" : "USD>CAD",
    "description" : f"The price of conversion would be: ${usdtocad}"
}

## Send post to prowlapp to inturn send to APNS
request = Request(url, urlencode(post_data).encode())
json = urlopen(request).read().decode()
print(json)