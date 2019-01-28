import math
import numpy as np
sqrtπ = math.sqrt(math.pi)
print('%s' % sqrtπ)
print('{}'.format(sqrtπ))
print(f'{sqrtπ}')

print()

print('%.3f' % sqrtπ)
print('{:.3f}'.format(sqrtπ))
print(f'{sqrtπ:.3f}')

print()

print('%6g' % sqrtπ)
print('{:6g}'.format(sqrtπ))
print(f'{sqrtπ:6g}')

print('   x   ', 'sin(x)  ', 'cos(x)', sep=' ')
for x in np.arange(-1, 1.05, 0.05):
    print(f'{x:7.4f} {math.sin(x):7.4f} {math.cos(x):7.4f}')
