#!/usr/bin/env python3

import sys
import subprocess

try:
    if 'tun0' in (subprocess.check_output(['nmcli','connection']).decode("utf-8")):
        nmcli_connection = ' Connection Secured'
    else:
        nmcli_connection = '%{F#ff0000} Connection Insecure%{F#ffffff}'
except:
        nmcli_connection = '%{F#ff0000} Connection Insecure%{F#ffffff}'

sys.stdout.write(nmcli_connection)
