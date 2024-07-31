class Estado:
    def __init__(self, pai, n):
        self.n = n
        self.pai = pai

def mostra_estado(estado):
    print(estado.n)

def estado_inicial():
    return Estado(None, 1)

def expandir(estado):
    if(estado.n >= 4):
        return[]
    return [Estado(estado, 2*estado.n), Estado(estado, 2*estado.n +1)]

def objectivo(estado):
    return False
def vazio(lista):
    return len(lista) == 0

def adiciona(filhos, lista):
   return lista + filhos

def recupera(lista):
    return lista.pop(0)

lista = [estado_inicial()]

while(not vazio(lista)):
    atual = recupera(lista)

    mostra_estado(atual)

    if(objectivo(atual)):
        mostra_estado(atual)
        break

    filhos = expandir(atual)
    lista = adiciona(filhos, lista)

# Para casa, mudar o algoritmo para busca em profundidade, muda while onde tem recupera, e adiciona

