#!/usr/bin/env python

import sys
import re

for line in sys.stdin:
    line = line.strip()

    words = re.findall(r"[\w']+", line)
    if len(words) == 1:
        print '%s\t%s' % (words[0], 1)
    for x in range(0,len(words)-1):
        first = words[x]
        second = words[x + 1]

        if first == second:
            continue
        print '%s-%s\t%s' % (first,second, 1)