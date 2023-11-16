nome = input('Digite seu nome ')
sexo = input('Digite seu sexo [M ou F] ')

if sexo == 'M':
    print(f'Seja bem vindo {nome}')
elif sexo == 'F':
    print(f'Seja bem vinda {nome}')
else:
    print(f'{sexo} Não é uma opção válida para sexo')
