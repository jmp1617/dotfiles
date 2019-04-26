#!/usr/bin/env python3

import sys
import subprocess

try:
    if 'tun0' in (subprocess.check_output(['nmcli','connection']).decode("utf-8")):
        icon = ''
    else:
        icon = ''
except:
    icon = ''

try:
    location = subprocess.check_output(['geo','-g']).decode("utf-8").split('\n')
    sys.stdout.write( icon + ' ' + location[2]+', '+location[0] )
except:
    sys.stdout.write('connecting ..')
