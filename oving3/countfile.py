#!/usr/bin/python3
import sys
import re

filepath = ''
if len(sys.argv) > 1:
    filepath = sys.argv[1]
else:
    filepath = 'out/out.txt'

pattern = re.compile('\w+')
with open(filepath, 'r') as file:
    total_words = 0
    for i, line in enumerate(file):
        temp = pattern.findall(line)
        print(temp)
        total_words += len(temp)
    print('words:', total_words)
    print('lines:', i+1)
        
