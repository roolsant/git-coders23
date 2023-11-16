soma = 0

for i in range(1, 5):
    nota = float(input(f'Digite a nota {i}: '))

    soma = soma + nota
    media = soma / 4

print(f'Pontuação total {soma}')
print(f'A média foi de {media:.2f}')

if media <= 5:
    print('⛔ REPROVADO')
elif media == 6:
    print('🟡 RECUPERAÇÃO')
else:
    print('🟢 APROVADO')
