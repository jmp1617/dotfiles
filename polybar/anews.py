#!/usr/bin/python
# Depends on python-feedparser
# Read Arch Linux RSS news;

import feedparser
from subprocess import call
import re
import textwrap


d = feedparser.parse("https://hnrss.org/newest")

for f in range(0,1):
    print( d.entries[f].title, )
    xy = d.entries[f].title
