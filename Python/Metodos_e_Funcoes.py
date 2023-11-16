lista = [1, 3, 12, 8, 2, 3, 2, 3]
lista2 = ['A', 70, 'X']
print(f'Lista antes do append : {lista}')

# append - Adicionando elementos ao final de uma lista
lista.append(3)
print(f'Lista após o append : {lista}')

# insert - Adicionando elementos em uma lista em posição definida
lista.insert(2, 10)
print(f'Lista após o insert : {lista}')

# extend - Unindo duas litas, insere os novos elemento ao final da lista
lista.extend(lista2)
print(f'Unindo lista com lista2 : {lista}')

# pop - Remove o índice especifico ou o ultimo indíce
# quando nenhum for especificado
lista.pop()
print(f'Lista após o pop : {lista}')

lista.pop(2)
print(f'Lista após o pop, removendo índice 2 : {lista}')

# remove - Remove um elemento específico de uma lista
# # [sempre o primero, caso o item se repita na lista]
lista.remove('A')
print(f'Lista após usar o remove para remover o "A" : {lista}')

# count - Conta quantas vezes um elemento se repete na lista
print(f'O item "3" aparece {lista.count(3)} vezes')

# index - Informa o Índice de um elemento na lista
print(f'Posição do "12" na lista : {lista.index(12)}')

# sort - Ordena a sua lista de forma Crescente
lista.sort()
print(f'Lista em ordem crescente : {lista}')

# sort - Ordena a sua lista de forma Decrescente
lista.sort(reverse=True)
print(f'Lista em ordem decrescente : {lista}')

# sum - Soma todos os elementos de uma lista
print(f'A soma dos elementos da lista é {sum(lista)}')

# min - Retorna o menor valor dentro de uma lista
print(f'O menor valor da lista é {min(lista)}')

# max - Retorna o maior valor dentro de uma lista
print(f'O maior valor da lista é {max(lista)}')
