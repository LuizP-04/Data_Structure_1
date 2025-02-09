class UPA:
    def __init__(self, unidade):
        self.unidade = unidade
        self.tamanhoFilaEspera = 0
        self.inicio = None
        
    def incluirPacienteNaFilaDeEspera(self, paciente):
        if paciente.criterio_risco is None:
            return None
        
        if self.inicio is None:
            self.inicio = paciente
        else:
            aux = self.inicio
            while aux.paciente_posterior != None:
                aux = aux.paciente_posterior
            aux.paciente_posterior = paciente
            paciente.paciente_anterior = aux
            
        self.tamanhoFilaEspera += 1
        
    def chamarPaciente(self):
        prioridade = {"BAIXO": 1, "MEDIO": 2, "ALTO": 3, "URGENTE": 4}
        aux = self.inicio
        removido = self.inicio
        maior = prioridade[removido.criterio_risco]
        while aux != None:
            if prioridade[aux.criterio_risco] > maior:
                maior = prioridade[aux.criterio_risco]
                removido = aux
            aux = aux.paciente_posterior
        
        if removido == self.inicio:
            self.inicio = removido.paciente_posterior
            if self.inicio != None: self.inicio.paciente_anterior = None
            removido.paciente_posterior = None
        
        else:
            removido.paciente_anterior.paciente_posterior = removido.paciente_posterior
            if removido.paciente_posterior != None: removido.paciente_posterior.paciente_anterior = removido.paciente_anterior
            removido.paciente_posterior = None
            removido.paciente_anterior = None
        
        self.tamanhoFilaEspera -= 1
        return removido
        
    def __str__(self):
        saida = ''
        aux = self.inicio
        if self.inicio is None: return '[]'
        while aux != None:
            saida += aux.__str__()
            aux = aux.paciente_posterior
        return saida
    