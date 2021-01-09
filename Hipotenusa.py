import math

cat1 = float(input('digite o cateto oposto: '))
cat2 = float(input('digite o cateto adjacente: '))
hp = math.hypot(cat1, cat2)
print(hp)