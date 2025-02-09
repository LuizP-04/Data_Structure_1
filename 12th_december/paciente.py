class Paciente:
    def __init__(self, nome, capacidade_procedimentos=5):
        self.nome = nome
        self.criterio_risco = None
        self.procedimentos = []
        self.capacidade_procedimentos = capacidade_procedimentos
        self.total_procedimentos = 0
        self.foi_atendido = False
        self.esta_liberado = False
        self.paciente_posterior = None
        self.paciente_anterior = None
        
    def mudarCriterio(self, novo):
        self.criterio_risco = novo
        
    def agendarMedicacao(self, medicacao):
        self.procedimentos.append(medicacao)
        self.total_procedimentos += 1
        self.foi_atendido = True
        
    def agendarExame(self, exame):
        self.procedimentos.append(exame)
        self.total_procedimentos += 1
        self.foi_atendido = True
        
    def executarProximoProcedimento(self):
        removido = self.procedimentos[self.total_procedimentos - 1]
        del self.procedimentos[self.total_procedimentos - 1]
        self.total_procedimentos -= 1
        return removido
    
    def listarProcedimentos(self):
        saida = ''
        for i in range(self.total_procedimentos):
            saida += self.procedimentos[i].nome
            if i != self.total_procedimentos-1: saida += ','
        return saida
    
    def proximoProcedimento(self):
        return self.procedimentos[self.total_procedimentos - 1]
    
    def estaLiberado(self):
        return self.total_procedimentos == 0 and self.foi_atendido == True
    
    def __str__(self):
        if self.criterio_risco is None: return f"[{self.nome}:NAO DEFINIDO]"
        return f"[{self.nome}:{self.criterio_risco}]"