alunos = dict()

for i in range(2):
    nome = input('Informe o nome do aluno: ')
    media = float(input('Informe a media do aluno: '))

    if media >= 7:
        situação = 'Aprovado'
    else:
        situação = 'Reprovado'

    alunos[nome] = situação
    #alunos[nome] = media

print(alunos)


