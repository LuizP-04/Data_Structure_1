class Eleicoes:
    
    def __init__(self, cidade):
        self.cidade = cidade
        self.raiz = None

    def adicionarR(self, ref, c):
        if ref.numero < c.numero:
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

