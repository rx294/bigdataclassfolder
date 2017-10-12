#!/usr/bin/env python

import sys
import re

for line in sys.stdin:
    line = line.strip()

    words = re.findall(r"[a-z0-9]+", line)
    words.append('')
    if len(words) == 1:
        print '%s\t%s' % (words[0], 1)
    for x in range(0,len(words)-1):
        first = words[x]
        second = words[x + 1]

        print '%s %s\t%s' % (first.lower(),second.lower(), 1)
