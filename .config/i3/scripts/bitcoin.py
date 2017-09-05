#!/usr/bin/env python3

import requests

print(requests.get(url='https://api.coindesk.com/v1/bpi/currentprice/usd.json').json()['bpi']['USD']['rate'].split('.')[0],"")
