import random

class No:

	def __init__(self,valor):
		self.esquerda = None
		self.direita = None
		self.ant = None
		self.valor = valor


class Arvore:

	def __init__(self):
		self.raiz = None

	def inserir(self,no):

		if self.raiz == None:
			self.raiz = no

		else:
			aux = self.raiz

			while aux.esquerda != None or aux.direita != None:

				if aux.valor < no.valor:
					if aux.esquerda == None:
						aux.esquerda = no
						break
					aux = aux.esquerda
				else:
					if aux.direita == None:
						aux.direita = no 
						break
					aux = aux.direita

	def inserirR(self,ref,no):

		if self.raiz == None:
			self.raiz = no 
		else:
			if ref.valor > no.valor:
				if ref.esquerda == None:
					ref.esquerda = no 
				else:
					self.inserirR(ref.esquerda,no)
			else:
				if ref.direita == None:
					ref.direita = no 
				else:
					self.inserirR(ref.direita,no)

	def emOrdem(self,ref):

		if ref == None:
			return ""

		self.emOrdem(ref.esquerda)
		print(ref.valor,end=",")
		self.emOrdem(ref.direita)
		

	def preOrdem(self,ref):
		if ref == None:
			return ""

		print(ref.valor,end=",")
		self.preOrdem(ref.esquerda)
		self.preOrdem(ref.direita)

	def posOrdem(self,ref):
		if ref == None:
			return ""

		
		self.posOrdem(ref.esquerda)
		self.posOrdem(ref.direita)
		print(ref.valor,end=",")


if "__main__":
	A = Arvore()

	
	vetor = [random.randint(1, 100) for _ in range(10)]
	print(vetor)
	for i in range(10):
		A.inserirR(A.raiz, No(vetor[i]))

	A.emOrdem(A.raiz)