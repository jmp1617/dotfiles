#!/usr/bin/env python3

import sys
import subprocess

ip = subprocess.check_output(['whereami','-f','human']).decode("utf-8").strip('\n')
ip = str(ip.split('\n')).split(',')
length = len(ip)
ip = ip[length-2].strip('\'').strip(' ')
sys.stdout.write( ip )
