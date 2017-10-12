#!/usr/bin/env python

import sys
import re

for line in sys.stdin:
    line = line.strip()

    words = re.findall(r"[a-z0-9]+", line)
    for x in range(0,len(words)):
        # first = words[x]
        # second = words[x + 1]
        if  (x + 1)<len(words):
            print '%s %s\t%s' % (words[x].lower(),words[x+1].lower(), 1)
        else:
            print '%s\t%s' % (words[x].lower(), 1)

