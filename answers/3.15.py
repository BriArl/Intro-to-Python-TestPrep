import math

f0 = float(input())

# Compute the ratio r
r = math.pow(2, 1/12)

# Calculate the frequencies of the next 3 keys
f1 = f0 * r
f2 = f0 * r**2
f3 = f0 * r**3

# Output the frequencies with two decimal places and units
print(f'{f0:.2f} Hz')
print(f'{f1:.2f} Hz')
print(f'{f2:.2f} Hz')
print(f'{f3:.2f} Hz')