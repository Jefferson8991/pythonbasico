'''
tabela ={'Alface': 0.45,
         'Batata': 1.20,
         'Tomate': 2.30,
         'Feijão': 1.50,}
print(tabela['Feijão'])
print(tabela['Batata'])
'''

#Atribuindo valores ao dicinario
'''
tabela ={'Alface': 0.45,
         'Batata': 1.20,
         'Tomate': 2.30,
         'Feijão': 1.50,}
tabela ['Milho'] = 3.0
tabela['Cebola'] = 1.25
tabela['Pipino'] = 4.00
print(tabela)
'''
# verificando se existe uma chave no dicionario
'''
comida ={'Alface': 0.45,
         'Batata': 1.20,
         'Tomate': 2.30,
         'Feijão': 1.50,}

valor = input('informe uma comida: ').title()

if valor in comida:
    print(comida[valor])
else:
    print('Não existe esse valor !')
'''
# Acessando valores com comandos keys e values
'''
tabela ={'Alface': 0.45,
         'Batata': 1.20,
         'Tomate': 2.30,
         'Feijão': 1.50,}
print(tabela.keys() )
print(tabela.values() )
'''
#iterando sobre as chaves e valores do dicionario
'''
tabela ={'Alface': 0.45,
         'Batata': 1.20,
         'Tomate': 2.30,
         'Feijão': 1.50,}

for chave, valor in tabela.items():
    print(chave, '->', valor )

'''
'''
comida = {'arroz': 20, 'macarrão': 30, 'Feijão': 40}

valores = comida.values()
print(min(valores))
print(max(valores))
print(sum(valores))
'''

# Deletando valores em uma lista
'''
Aluno = {'jefferson': 24, 'veronica': 25, 'Gael': 1}
idade = Aluno.values()
print('Esses são seus alunos {}'.format(Aluno))
print(' E a idade do aluno mais velho é {}'.format(max(idade)))
'''