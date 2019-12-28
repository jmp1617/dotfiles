#!/usr/bin/env python3

import sys
import subprocess
import json

try:
    if 'tun0' in (subprocess.check_output(['nmcli','connection']).decode("utf-8")):
        icon = ''
    else:
        icon = ''
except:
    icon = ''

try:
    external = subprocess.check_output(['curl','-s', 'https://ipinfo.io/ip']).decode("utf-8").strip("\n")
    geo_addr = "https://ipvigilante.com/" + str(external.strip(" "))
    location = subprocess.check_output(['curl','-s', str(geo_addr)]).decode("utf-8")
    geo = json.loads(location)
    print(icon + " " + geo["data"]["city_name"] + ", " + geo["data"]["subdivision_1_name"] + ", " + geo["data"]["country_name"])
except:
    print("Connecting...")
