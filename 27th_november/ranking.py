class Ranking:

	def __init__(self):
		self.inicio = None
		self.total_competidores = 0

	def inserir(self,c):
		if self.inicio == None:
			self.inicio = c
		elif self.inicio.pontuacao < c.pontuacao:
			c.direita = self.inicio
			self.inicio = c
		else:
			aux = self.inicio
			while aux.direita != None and aux.direita.pontuacao > c.pontuacao:
				aux = aux.direita
			c.direita = aux.direita
			aux.direita = c
		
		self.total_competidores += 1
		

	def __insereUnico(self,c):
		pass
		#use, caso ache util

	def __insereInicio(self,c):
		pass
		#use, caso ache util

	def __insereMeio(self,aux,c):
		pass
		#use, caso ache util


	def __insereFim(self,aux,c):
		pass
		#use, caso ache util

	def busca(self,nome):
		aux = self.inicio
		while aux != None:
			if aux.nome == nome:
				return aux
			else:
				aux = aux.direita


	def remover(self, nome):
		buscado = self.busca(nome)
 
		if buscado == self.inicio and self.total_competidores == 1:
			self.inicio = None
 
		elif buscado == self.inicio:
			self.inicio.direita.esquerda = None
			self.inicio.direita = None
			self.inicio = buscado.direita

 
		elif buscado.direita == None:
			buscado.esquerda.direita = None
			buscado.esquerda = None
 
		else:
			buscado.direita.esquerda = buscado.esquerda
			buscado.esquerda.direita = buscado.direita
			buscado.direita = None
			buscado.esquerda = None

		self.total_competidores -= 1


	def __str__(self):
		saida = ''
		aux = self.inicio
		if self.total_competidores == 0:
			saida = '[]'
			return saida
		else:
			while aux != None:
				saida+=f'[{aux.nome}:{aux.pontuacao}]'
				aux = aux.direita
			return saida
