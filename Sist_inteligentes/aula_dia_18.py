class Estado:
    def __init__(self, pai, n, a, b, c):
        self.pai = pai
        self.n = n
        self.a = a
        self.b = b
        self.c = c

def mostra_estado(estado):
    print(f"n: {estado.n}, a: {estado.a}, b: {estado.b}, c: {estado.c}")

def estado_inicial():
    return Estado(None, [1, 3, 7], [], [], [])

def move(estado, origem, destino):
    if origem and (not destino or origem[-1] < destino[-1]):
        novo_origem = origem[:-1]
        novo_destino = destino + [origem[-1]]
        return Estado(estado, estado.n, novo_origem, novo_destino, estado.c) if destino is estado.b else Estado(estado, estado.n, novo_origem, estado.b, novo_destino)
    return None

def expandir(estado):
    filhos = []
    if estado.a:
        filhos.append(move(estado, estado.a, estado.b))
        filhos.append(move(estado, estado.a, estado.c))
    if estado.b:
        filhos.append(move(estado, estado.b, estado.a))
        filhos.append(move(estado, estado.b, estado.c))
    if estado.c:
        filhos.append(move(estado, estado.c, estado.a))
        filhos.append(move(estado, estado.c, estado.b))
    return [filho for filho in filhos if filho is not None]

def objectivo(estado):
    return estado.c == [1, 3, 7]

def vazio(lista):
    return len(lista) == 0

def adiciona(filhos, lista):
    return filhos + lista  # Para busca em profundidade

def recupera(lista):
    return lista.pop(0)

def mostra_caminho(estado):
    if estado is None:
        return
    mostra_caminho(estado.pai)
    mostra_estado(estado)

lista = [estado_inicial()]

while not vazio(lista):
    atual = recupera(lista)

    if objectivo(atual):
        mostra_caminho(atual)
        break

    filhos = expandir(atual)
    lista = adiciona(filhos, lista)
