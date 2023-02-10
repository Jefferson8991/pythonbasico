#Teste comando if
    #if é um comando de condição = Quando ele é utilizado é necessário após seu uso incluir um bloco que seja verdadeiro!

    # Condição verdadeira

""" idade = 17

if idade < 18:
    print("Menor de idade!")

print("Fim.") """

    #Condição Falsa

""" idade = 100

if idade < 18:
    print("Menor de idade!")

print("Fim.") """

    #Exemplo de if com condições - neste exemplo o if a ser considerado será o que for maior nas variáveis com input


""" a = int(input("Primeiro Valor:"))
b = int(input("Segundo Valor:"))

if a > b:
    print("O primeiro núemro é o Maior!")

if a < b:
    print("O segundo número é o maior!") """

    #Exemplo de if + else

""" a = int(input("Primeiro Valor:"))
b = int(input("Segundo Valor:"))

if a > b:
    print("O primeiro núemro é o Maior!")

else:
    print("O segundo número é o maior!") """

    #Exemplo de Estrutura aninhada

minutos = int(input("Digite a quantidade minutos utilizados no mês:"))
preco = 0

if minutos < 200:
    preco = 0.15
else:
    if minutos > 200 and minutos < 400:
        preco = 0.18    
    else:
        preco = 0.20

cal = minutos * preco

print(f"O valor da fatura é R${cal}")