agenda = dict()
while True:
    
        nome = input('Nome: ')
        contato = int(input('Contato: '))
        agenda[nome] = contato  
    
        ver = input('deseja sair : ')
    
        if ver == 'sair':
            break
        
            
print(agenda)

