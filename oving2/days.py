#!/usr/bin/python3
days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
print(*days, sep=', ')
print(', '.join(days))
print('lengde', len(days))
print(*sorted(days), sep=', ')
