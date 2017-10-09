#!/usr/bin/env python

import sys
import re

for line in sys.stdin:
    line = line.strip()

    words = re.findall(r"[\w']+", line)
    for x in range(0,len(words)-1):
        first = words[x]
        second = words[x + 1]

        if first == second:
            continue
        print '%s-%s\t%s' % (first,second, 1)