class Estado:
	def __init__(self, pai, profundidade, n):
		self.n = n
		self.pai = pai
		self.profundidade = profundidade

def mostra_estado(estado):
	print(estado.n)

def estado_inicial():
	return Estado(None, 0, 1)

def expande(estado):
	if(estado.n >= 4):
		return []
	profundidade = estado.profundidade + 1
	return [Estado(estado, profundidade, 2*estado.n), Estado(estado, profundidade, 2*estado.n + 1)]

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
	return filhos + lista

def recupera(lista):
	return lista.pop(0)

lista = [estado_inicial()]
limite = 1


print("Explorando estados: ")
while(not vazio(lista)):
	atual = recupera(lista)

	mostra_estado(atual)

	if(objetivo(atual)):
		print("Solução encontrada: ")
		mostra_caminho(atual)
		break
	if(atual.profundidade == limite):
		continue


	filhos = expande(atual)
	lista = adiciona(filhos, lista)