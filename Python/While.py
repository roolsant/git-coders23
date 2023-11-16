chave_usuario = input('Digite um numero entre 0 e 100 --->')
chave = 33
chave_digitada = int(chave_usuario)

while chave_digitada != chave:
    print(f'⛔ Infelizmente {chave_digitada} não é a chave')
    chave_usuario = input('Digite um numero entre 0 e 100 --->')
    chave_digitada = int(chave_usuario)

if chave_digitada == chave:
    print(f'🟢 Parabéns, {chave_digitada} é o número chave!')
