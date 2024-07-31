class Estado:
	def __init__(self, pai, n):
		self.n = n
		self.pai = pai

def mostra_estado(estado):
	print(estado.n)

def estado_inicial():
	return Estado(None, 1)

def expande(estado):
	if(estado.n >= 4):
		return []
	return [Estado(estado, 2*estado.n), Estado(estado, 2*estado.n + 1)]

def objetivo(estado):
	return estado.n == 7

def mostra_caminho(estado):
	if(estado == None):
		return
	mostra_caminho(estado.pai)
	mostra_estado(estado)

def vazio(lista):
	return len(lista) == 0

def adiciona(filhos, lista):
	return lista + filhos

def recupera(lista):
	return lista.pop(0)

lista = [estado_inicial()]

print("Explorando estados: ")
while(not vazio(lista)):
	atual = recupera(lista)

	mostra_estado(atual)

	if(objetivo(atual)):
		print("Solução encontrada: ")
		mostra_caminho(atual)
		break

	filhos = expande(atual)
	lista = adiciona(filhos, lista)