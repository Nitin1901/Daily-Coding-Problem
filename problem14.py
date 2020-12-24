import random
import decimal

c, s = 0, 0
for i in range(10000):
    s += 1
    x = float(decimal.Decimal(random.randrange(-100, 100))/100)
    y = float(decimal.Decimal(random.randrange(-100, 100))/100)
    if (x**2+y**2 <= 1):
        c += 1
    if i%1000 == 0:
        pi = 4*c/s
        print(pi)
pi = 4*c/s
print(pi)