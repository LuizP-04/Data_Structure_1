class Candidato:

    def __init__(self, nome, numero, votos):
        self.nome = nome
        self.numero = numero
        self.votos = votos
        self.antecessor = None
        self.direita = None
        self.esquerda = None
        