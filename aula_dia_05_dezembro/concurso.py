class Concurso:
    
    def __init__(self, concurso):
        self.concurso = concurso
        self.primeiro_inscrito = None
        self.inscritos = 0
    
    def inscrever(self, c):
    
        if self.primeiro_inscrito == None:
            self.primeiro_inscrito = c
            self.primeiro_inscrito.posterior = c
            self.primeiro_inscrito.anterior = c
        else:
            aux = self.primeiro_inscrito
            if self.inscritos == 1:
                aux.posterior = c
                aux.anterior = c
                c.anterior = aux
                c.posterior = aux
            else:
                aux.anterior.posterior = c
                c.anterior = aux.anterior
                aux.anterior = c 
                c.posterior = aux
                    
        self.inscritos += 1

    def busca(self, nome):
        aux =  self.primeiro_inscrito
        if nome !=None:
            if self.inscritos == 0:
                return None
            elif self.inscritos == 1 and aux.nome != nome:
                return None
            elif self.inscritos == 1 and aux.nome == nome:
                return aux
            else:
                aux_cont = self.inscritos
                while aux_cont != 0:
                    if aux.nome == nome:
                        return aux
                    else:
                        aux = aux.posterior
                    aux_cont-=1
    def buscar_p_i(self, pontuacao=''):
        aux = self.primeiro_inscrito
        if pontuacao == 'Par':
            if self.inscritos == 0:
                return None
            elif self.inscritos == 1 and aux.pontuacao%2!=0:
                return None
            elif self.inscritos == 1 and aux.pontuacao%2==0:
                return aux
            else:
                aux_cont = self.inscritos
                while aux_cont != 0:
                    if aux.pontuacao%2==0:
                        return aux
                    else:
                        aux = aux.posterior
                    aux_cont-=1
        elif pontuacao == 'Impar':
            if self.inscritos == 0:
                return None
            elif self.inscritos == 1 and aux.pontuacao%2==0:
                return None
            elif self.inscritos == 1 and aux.pontuacao%2!=0:
                return aux
            else:
                aux_cont = self.inscritos
                while aux_cont != 0:
                    if aux.pontuacao%2!=0:
                        return aux
                    else:
                        aux = aux.posterior
                    aux_cont-=1



    def remove(self, nome='', pontuacao=''):
        buscado = self.busca(nome)
        buscadoi = self.buscar_p_i(pontuacao='')
        if pontuacao=='Par':
            if buscadoi == None:
                return False
            elif buscadoi == self.primeiro_inscrito and self.inscritos == 1:
                self.primeiro_inscrito.anterior = None
                self.primeiro_inscrito.posterior = None
                self.primeiro_inscrito = None
                self.inscritos-=1
                return True
            elif buscadoi == self.primeiro_inscrito:
                buscadoi.anterior.posterior = buscadoi.posterior
                buscadoi.posterior.anterior = buscadoi.anterior
                self.primeiro_inscrito = buscadoi.posterior
                buscadoi.posterior = None
                buscadoi.anterior = None
                self.inscritos-=1
                return True
            else:
                buscadoi.anterior.posterior = buscadoi.posterior
                buscadoi.posterior.anterior = buscadoi.anterior
                buscadoi.posterior = None
                buscadoi.anterior = None
                self.inscritos-=1
                return True 
        if pontuacao=='Impar':
            if buscadoi == None:
                return False
            elif buscadoi == self.primeiro_inscrito and self.inscritos == 1:
                self.primeiro_inscrito.anterior = None
                self.primeiro_inscrito.posterior = None
                self.primeiro_inscrito = None
                self.inscritos-=1
                return True
            elif buscadoi == self.primeiro_inscrito:
                buscadoi.anterior.posterior = buscadoi.posterior
                buscadoi.posterior.anterior = buscadoi.anterior
                self.primeiro_inscrito = buscado.posterior
                buscadoi.posterior = None
                buscadoi.anterior = None
                self.inscritos-=1
                return True
            else:
                buscadoi.anterior.posterior = buscadoi.posterior
                buscadoi.posterior.anterior = buscadoi.anterior
                buscadoi.posterior = None
                buscadoi.anterior = None
                self.inscritos-=1
                return True 
        else:
            if buscado == None:
                return False
            elif buscado == self.primeiro_inscrito and self.inscritos == 1:
                self.primeiro_inscrito.anterior = None
                self.primeiro_inscrito.posterior = None
                self.primeiro_inscrito = None
                self.inscritos-=1
                return True
            elif buscado == self.primeiro_inscrito:
                buscado.anterior.posterior = buscado.posterior
                buscado.posterior.anterior = buscado.anterior
                self.primeiro_inscrito = buscado.posterior
                buscado.posterior = None
                buscado.anterior = None
                self.inscritos-=1
                return True
            else:
                buscado.anterior.posterior = buscado.posterior
                buscado.posterior.anterior = buscado.anterior
                buscado.posterior = None
                buscado.anterior = None
                self.inscritos-=1
                return True
        
    def candidatos(self):
        aux = self.primeiro_inscrito
        aux_cont = self.inscritos
        lista = []
        if self.inscritos == 0:
            lista = []
        else:
            while aux_cont != 0:
                lista.append(aux.nome)
                aux = aux.posterior
                aux_cont-=1
        lista.sort()
        saida = lista
        return saida

    
    def __str__(self):
        saida = ''
        aux = self.primeiro_inscrito
        aux_cont = self.inscritos
        saida = f'{self.concurso}'
        if self.inscritos == 0:
            saida+='[]'
        elif self.inscritos == 1:
            saida+= f'{aux}'
        else:
            while aux_cont != 0:
                saida+=f'{aux}'
                aux = aux.posterior
                aux_cont-=1
                
        return saida