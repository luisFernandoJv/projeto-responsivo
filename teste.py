
cerveja = ['skol', 'cana', 'triunfo']
liente = []

def cliente():
    
    for i in range(3):
        
        pedido = input('digite seu pedido vc tem 3 opções: ')
        liente.append(pedido)
        
    adiciona_valor()

def ber():
    
        cerv = input('Digite o tipo de cerveja: ')
        
        if(cerv == 'skol' or cerv == 'cana' or cerv == 'triunfo'):
            
            print('tenho sua cerveja\n')
            
            liente.append(cerv)
            
            return
        else:
            print('não tenho sua cerveja')
def total():
    pedido_total = liente
    print(f'seu pedido total foi:\n')
    
    for i in pedido_total:
        print(i)
    
    print('obrigado\n')
    
def adiciona_valor():
    
    valor = input('Seu valor total foi de:\n')
    
    liente.append(valor) 
    
    
ber()
cliente()
total()