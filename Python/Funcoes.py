# funcao inicial
nome_aluno = input('Digite seu nome :')
seu_curso = input('Digite seu curso: ')


def saudacao(nome=nome_aluno, curso=seu_curso):
    print(f'Seja bem vinda(o)!{nome} ao curso de {curso}')


saudacao(nome_aluno, seu_curso)
