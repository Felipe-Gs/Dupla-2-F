import math
a = int(input('digte o valor de a:'))
if a == 0:
    print('a equação não é do segundo grau!!!')
b = int(input('digite o valor de b:'))
c = int(input('digite o valor de c:'))
delta = (-b*-b)-(4*a*c)
if delta <= 0:
    print('nao possui raizes reais')
    exit()
raiz = math.sqrt(delta)
x1 = (-b + raiz)/(2*a)
x2 = (-b - raiz)/(2*a)
if delta <= 0:
    print('a equacao não possui raizes reais....')
elif delta == 0:
    print('a equação possui uma raiz real.....')
elif delta >= 0:
    print('a equação possui duas raizes...')
print(f'o valor de delta é {delta}')
print(f'o valor de x1 é {x1}')
print(f'o valor de x2 é {x2}')