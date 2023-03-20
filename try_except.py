a = 10
b = 0

try:
    print(a/b)
except ZeroDivisionError as error:
    print('Não pode diviir por 0 ', error)
