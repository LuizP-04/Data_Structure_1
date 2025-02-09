class Eleicoes:
    
    def __init__(self, cidade):
        self.cidade = cidade
        self.raiz = None


    def adicionarR(self, ref, c):
        if ref.numero <= c.numero:
            if ref.direita == None:
                ref.direita = c
                c.antecessor = ref
            else:
                self.adicionarR(ref.direita, c)
        else:
            if ref.esquerda == None:
                ref.esquerda = c
                c.antecessor = ref
            else:
                self.adicionarR(ref.esquerda, c)
    def adicionarCandidato(self, candidato):
        if self.raiz == None:
            self.raiz = candidato
        else:
            self.adicionarR(self.raiz, candidato)
    

    def emOrdem(self, ref):
        if ref == None:
            return ''
        return self.emOrdem(ref.esquerda) + str(ref.numero) + ',' + self.emOrdem(ref.direita)
    def em_ordem(self):
        return self.emOrdem(self.raiz)[:-1]
    

    def preOrdem(self, ref):
        if ref == None:
            return ''
        return str(ref.numero)+','+ self.preOrdem(ref.esquerda) + self.preOrdem(ref.direita)
    def pre_ordem(self):
        return self.preOrdem(self.raiz)[:-1]
    

    def posOrdem(self, ref):
        if ref == None:
            return ''
        return self.posOrdem(ref.esquerda)+self.posOrdem(ref.direita)+str(ref.numero)+','
    def pos_ordem(self):
        return self.posOrdem(self.raiz)[:-1]
    

    def auxstr(self, ref):
        if ref == None:
            return ''
        return'('+self.auxstr(ref.esquerda)+str(ref.numero)+self.auxstr(ref.direita)+')'
    def __str__(self):
        if self.raiz == None:
            return '()'
        return self.auxstr(self.raiz)
    

    def auxbusca(self, ref, buscado):
        if ref == None:
            return 'Não achado'
        elif ref.numero>buscado:
            return self.auxbusca(ref.esquerda, buscado)
        elif ref.numero<buscado:
            return self.auxbusca(ref.direita, buscado)
        else:
            return ref
    def busca(self, buscado):
        return self.auxbusca(self.raiz, buscado)
    

    def auxcontacandidatos(self, ref):
        if ref == None:
            return 0
        return self.auxcontacandidatos(ref.esquerda)+self.auxcontacandidatos(ref.direita)+1
    def contaCandidatos(self):
        return self.auxcontacandidatos(self.raiz)
    def contaCandidatosRecursivo(self, ref):
        if ref == None:
            return 0
        return self.contaCandidatosRecursivo(ref.esquerda)+self.contaCandidatosRecursivo(ref.direita)+1

    def auxsucessor(self, ref, valor):
        if ref.esquerda == None:
            return ref
        elif ref.esquerda != None:
            return self.auxsucessor(ref.esquerda, valor)
    def sucessor(self, valor):
        loc = self.auxbusca(self.raiz, valor)
        if loc == None:
            return None
        elif loc.direita == None:
            return None
        else:
            return self.auxsucessor(loc.direita, valor)

    
    def auxantecessor(self, ref, valor):
        if ref.direita == None:
            return ref
        elif ref.direita != None:
            return self.auxantecessor(ref.direita, valor)
    def antecessor(self, valor):
        loc = self.auxbusca(self.raiz, valor)
        if loc == None:
            return None
        elif loc.esquerda == None:
            return None
        else:
            return self.auxantecessor(loc.esquerda, valor)


    def remover(self, valor):
        removido = self.busca(valor)
        sucessor = self.sucessor(valor)
        antecessor = self.antecessor(valor)
        if removido.direita == None and removido.esquerda == None and removido.antecessor == None:
            self.raiz = None
        elif removido.direita == None and removido.esquerda == None:
            if removido.numero<= self.raiz.numero:
                removido.antecessor.esquerda = None
                removido.antecessor = None
            else:
                removido.antecessor.direita = None
                removido.antecessor = None
        elif self.raiz == removido :
            if self.raiz.direita != None:
                if sucessor.numero <= sucessor.antecessor.numero:
                    sucessor.antecessor.esquerda = None
                else:
                    sucessor.antecessor.direita = None
                if sucessor.direita != None:
                    if sucessor.direita.numero > sucessor.numero:
                        sucessor.direita.antecessor = sucessor.antecessor
                        if sucessor.antecessor.numero >= sucessor.direita.numero:
                            sucessor.antecessor.esquerda = sucessor.direita
                        else:
                            sucessor.antecessor.direita = sucessor.direita
                sucessor.esquerda = self.raiz.esquerda
                sucessor.direita  =  self.raiz.direita
                if self.raiz.direita != None:
                    self.raiz.direita.antecessor = sucessor
                if self.raiz.esquerda != None:
                    self.raiz.esquerda.antecessor = sucessor
                sucessor.antecessor = None
                self.raiz = sucessor
            else:
                if antecessor.numero <= antecessor.antecessor.numero:
                    antecessor.antecessor.esquerda = None
                else:
                    antecessor.antecessor.direita = None
                if antecessor.esquerda != None:
                    antecessor.esquerda.antecessor = antecessor.antecessor
                    antecessor.antecessor.esquerda = antecessor.esquerda
                    
                antecessor.esquerda = self.raiz.esquerda
                antecessor.direita  =  self.raiz.direita
                if self.raiz.direita != None:
                    self.raiz.direita.antecessor = antecessor
                if self.raiz.esquerda != None:
                    self.raiz.esquerda.antecessor = antecessor
                self.raiz = antecessor
        elif removido.numero > self.raiz.numero:
            if removido.direita != None:
                sucessor.antecessor = removido.antecessor
                removido.antecessor.direita = sucessor
                removido.direita = None
        elif removido.numero<=self.raiz.numero:
            if sucessor.antecessor.numero > sucessor.numero:
                sucessor.antecessor.esquerda = None
                sucessor.antecessor = None
            if removido.esquerda !=  None:
                sucessor.esquerda = removido.esquerda
            sucessor.direita = removido.direita
            sucessor.antecessor = removido.antecessor
            if removido.antecessor.numero > removido.numero:
                removido.antecessor.esquerda = sucessor
            else:
                removido.antecessor.direita = sucessor