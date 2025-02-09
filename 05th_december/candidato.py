class Candidato:
    
    def __init__(self, nome, nota=0):
        self.nome = nome
        self.nota = nota
        self.posterior = None
        self.anterior = None
    
    def __str__(self):
        saida = ''
        saida += f'[{self.nome}:{self.nota}]'
        return saida
    
    