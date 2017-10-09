#!/usr/bin/env python

import sys
import re

# input comes from STDIN (standard input)
for line in sys.stdin:
    # remove leading and trailing whitespace
    line = line.strip()

    # split the line into words
    words = re.findall(r"[\w']+", line)
    # increase counters
    for x in range(0,len(words)-1):
        # write the results to STDOUT (standard output);
        # what we output here will be the input for the
        # Reduce step, i.e. the input for reducer.py
        #
        # tab-delimited; the trivial word count is 1
        first = words[x]
        second = words[x + 1]

        if first == second:
            continue
        print '%s-%s\t%s' % (first,second, 1)