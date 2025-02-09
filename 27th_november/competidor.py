class Competidor:
	def __init__(self, c, pontuacao=0):
		self.nome = c
		self.direita = None
		self.esquerda = None
		self.pontuacao = pontuacao
	def alterarPontuacao(self, new):
		self.pontuacao = self.pontuacao + new
	def __str__(self):
		self.__str__ = f'[{self.nome}:{self.pontuacao}]'
		return self.__str__