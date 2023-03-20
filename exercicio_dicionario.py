# programa: Preços de mercadorias
# par 1 - programa que permite que o usuario cadastre produto e valores
# parte 2 - mostrar a tabela na tela

mercado = dict()

for i in range(2):
    
    produto = str(input('informe um item: '))
    valor = float(input('informe um valor: '))
    mercado[produto] = valor
print(mercado)

while True:
    produtodesejado = input('Informe um produto ou 0 para sair')
    if produtodesejado in mercado:
        print(mercado[produtodesejado])

    elif produtodesejado == '0':
        break
    else:
        print('Produto não existe, informe um produto existente. ')


