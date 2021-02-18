altura = []
sexo = []
mulheres = []
homens = []

for c in range(3):
    alt = float(input('digite sua altura:'))
    altura.append(alt)
    sx = input('digite seu sexo:').strip().upper()[0]
    if sx == 'F':
        mulheres.append(alt)
    elif sx == 'M':
        homens.append(alt)

soma = sum(mulheres)
media = soma/len(mulheres)
    
menor = min(altura) 
maior = max(altura)       
print('as alturas sao:', altura)

print('altura dos homens sao:', homens)
print('altura das mulheres sao:', mulheres)
print('a menor altura do grp é:', menor)
print('a maior altura do grupo é:', maior)
print('a media da altura entre as mulheres é {:.2f}'.format(media))
print('O numero de homens na lista é: ', len(homens))
