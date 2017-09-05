#!/usr/bin/env python3

import requests

mine = requests.get(url="https://ethermine.org/api/miner_new/B0b359582fEb5973178D0c6CfBBE59474c69e207").json()

hashrate = mine['workers']['glados']['hashrate']
unpaid = int(str(mine['unpaid'])[:3])/10000

print(hashrate,unpaid,"")
