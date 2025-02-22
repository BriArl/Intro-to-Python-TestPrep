import math

f0 = float(input())

r = math.pow(2, 1/12)

f1 = f0 * r
f2 = f0 * r**2
f3 = f0 * r**3

print(f'{f0:.2f} Hz')
print(f'{f1:.2f} Hz')
print(f'{f2:.2f} Hz')
print(f'{f3:.2f} Hz')