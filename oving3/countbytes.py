#!/usr/bin/python3
import sys
import os

filepath = ''
if len(sys.argv) > 1:
    filepath = sys.argv[1]
else:
    filepath = 'out/out.txt'

print(os.path.getsize(filepath))
        
