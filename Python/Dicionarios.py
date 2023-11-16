dicionario = {'nome': 'Rodrigo', 'idade': '45', 'altura': '1.70'}

# acessar uma chave
print(dicionario['idade'])

# adicionando elementos a uma chave
dicionario['funcao'] = 'Developer'
print(dicionario)

# substituir um valor na chave
dicionario['nome'] = 'Rodrigo Santos'
print(dicionario)

# iterar sobre um dicionario
for i in dicionario:
    print(i, dicionario[i])

# testando a existencia de uma chave
print('peso' in dicionario)
