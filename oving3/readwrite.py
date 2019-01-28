#!/usr/bin/python3
from os import path 
with open(path.join('out', 'out.txt'), 'w') as file:
    file.write("Hello world\n")
    file.write("Skriver en linje til\n")
    file.write("Her kommer enda en linje\n")

with open(path.join('out', 'out.txt'), 'r') as file:
    next(file)
    print(file.readline(), end='')
    file.seek(0)
    print(file.read(10))
    
