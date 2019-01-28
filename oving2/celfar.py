def celciusFar(c):
    return c * (9/5) + 32

c = float(input("What's the current temperature? (in Celsius)\n"))
print(f'Det er {celciusFar(c):.1f}°F')

