""" nota1 = float(input("Informe a 1 nota:"))
nota2 = float(input("Informe a 2 nota: "))
nota3 = float(input("Informe a 3 nota: "))


media = (nota1 + nota2 + nota3)/3

print(media)



if media >= 7.0:
    print("aluno aprovado !")
else:
    print("aluno reprovado!")
 """

""" velocidade = float(input("Digite a sua veelocidade: "))

valormulta = (velocidade - 80)*5

if velocidade > 80:
    print("voce foi multado !")
    print(f"valor da multa e {valormulta}")
 """
 
""" parouimpar =  int(input("Digite o valor: "))

resto = parouimpar % 2

if resto == 0:
    print("numero par !")
else:
    print("numro impar !")
    print(f"seu numero é {resto}") """


a = int(input("digite o numero1: "))

maior = a
menor = a

b = int(input("digite o numero2: "))

if b > maior:
    maior = b

else:
    menor = b


c = int(input("digite o numero3: "))

if c > maior:
    maior = c

else:
    menor = c

print(maior)
print(menor)


