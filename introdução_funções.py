def convert(horas):
    segundos = horas * 3600
    minutos = horas * 60

    
  
    return segundos, minutos, 


#chamada
valorH = int(input('Informe as horas: '))
valorM = int(input('Informe os minutos: '))
#valorD = int(input('Informe a quantidade de dias: '))


print( convert(valorH))
print(convert(valorM))



