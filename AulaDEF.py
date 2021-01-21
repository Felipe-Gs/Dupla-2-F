''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
def media():
    nota1 = float(input('digite a nota 1:'))
    nota2 = float(input('digite a nota 2:'))
    media = (nota1 + nota2)/2
    print(media)

media()   


def m(a, b):
    media = a + b
    media = media/2
    print(media)

x = int(input('digite o valor:'))
y = int(input('digite o valor:'))
m(x, y) 

def linha(number):
    aux = 1
    lin =  ""
    while(aux <= number):
        lin = lin + str(number) 
        aux = aux + 1
    return lin    

def quest(number):
    aux = 1
    while(aux <= number):
        result = linha(aux)
        print(result)
        aux = aux + 1

x = int(input('digite o numero: '))
quest(x)



''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
def soma(a, b, c):
    s = a + b + c
    print(s)

x = int(input('digite o numero de a :'))
y = int(input('digite o numero de b :'))  
z = int(input('digite o numero de c :'))
soma(x, y, z)    