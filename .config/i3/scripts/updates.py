#!/usr/bin/env python3

import subprocess

print(str(subprocess.check_output(["checkupdates"]).decode("utf-8")).count('\n'),"")
