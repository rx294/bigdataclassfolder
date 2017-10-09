#!/usr/bin/env python

from operator import itemgetter
import sys

current_word_pair = None
current_word_pair_count = 0
word_pair = None

for line in sys.stdin:
    line = line.strip()

    word_pair, count = line.split('\t', 1)
    try:
        count = int(count)
    except ValueError:
        continue
    if current_word_pair == word_pair:
        current_word_pair_count += count
    else:
        if current_word_pair:
            print '%s\t%s' % (current_word_pair, current_word_pair_count)
        current_word_pair_count = count
        current_word_pair = word

if current_word == word:
    print '%s\t%s' % (current_word_pair, current_word_pair_count)