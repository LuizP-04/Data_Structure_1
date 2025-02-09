from candidato import Candidato
from eleicoes import Eleicoes  
from tratamentos import *


def teste1():


	try:
		c1 = Candidato("Joao",88834,1743)


	except Exception as a:
		return traduzMensagem(a)
	return 'OK'


def teste2():


	try:
		c1 = Candidato("Joao",88834,1743)
		assert c1.numero == 88834
		assert c1.votos == 1743


	except Exception as a:
		return traduzMensagem(a)
	return 'OK'




def teste3():


	try:
		c1 = Candidato("Joao",88834,1743)
		E = Eleicoes("Bitslandia")
	except Exception as a:
		return traduzMensagem(a)
	return 'OK'


def teste4():


	try:
		c1 = Candidato("Joao",88834,1743)
		E = Eleicoes("Bitslandia")
		E.adicionarCandidato(c1)
	except Exception as a:
		return traduzMensagem(a)
	return 'OK'


def teste5():
	try:
		c1 = Candidato("Joao",88834,1743)
		E = Eleicoes("Bitslandia")
		E.adicionarCandidato(c1)
		assert E.raiz == c1
	except Exception as a:
		return traduzMensagem(a)
	return 'OK'


def teste6():
	try:
		c1 = Candidato("Joao",88834,1743)
		c2 = Candidato("Joao",58834,1743)
		E = Eleicoes("Bitslandia")
		E.adicionarCandidato(c1)
		E.adicionarCandidato(c2)
		assert E.raiz.esquerda == c2
		assert E.raiz.direita == None
	except Exception as a:
		return traduzMensagem(a)
	return 'OK'


def teste7():
	try:
		c1 = Candidato("Joao",88834,1743)
		c2 = Candidato("Joao",58834,1743)
		E = Eleicoes("Bitslandia")
		E.adicionarCandidato(c1)
		E.adicionarCandidato(c2)
		assert c2.antecessor == c1


	except Exception as a:
		return traduzMensagem(a)
	return 'OK'




def teste8():
	try:
		c1 = Candidato("Joao",88834,1743)
		c2 = Candidato("Joao",58834,1743)
		c3 = Candidato("Joao",92834,1743)
		c4 = Candidato("Joao",54834,1743)
		c5 = Candidato("Joao",87834,1743)
		cs = [c1,c2,c3,c4,c5]
		E = Eleicoes("Bitslandia")
		for i in cs:
			E.adicionarCandidato(i)


		assert c4.antecessor.antecessor == E.raiz
		assert c4.antecessor.antecessor.direita == c3


	except Exception as a:
		return traduzMensagem(a)
	return 'OK'


def teste9():
	try:
		c1 = Candidato("A",50000,550)
		c2 = Candidato("B",40000,31743)
		c3 = Candidato("C",60000,1343)
		c4 = Candidato("D",30000,1943)
		c5 = Candidato("D",45000,43)
		c6 = Candidato("E",55000,17843)
		c7 = Candidato("F",65000,13)
		cs = [c1,c2,c3,c4,c5,c6,c7]
		E = Eleicoes("Bitslandia")
		for i in cs:
			E.adicionarCandidato(i)


		assert c1.esquerda.esquerda.antecessor.direita == c5
		assert c7.antecessor.esquerda.antecessor.antecessor == c1


	except Exception as a:
		return traduzMensagem(a)
	return 'OK'




def teste10():
	try:
		c1 = Candidato("A",50000,550)
		c2 = Candidato("B",40000,31743)
		c3 = Candidato("C",60000,1343)
		c4 = Candidato("D",30000,1943)
		c5 = Candidato("D",45000,43)
		c6 = Candidato("E",55000,17843)
		c7 = Candidato("F",65000,13)
		cs = [c1,c2,c3,c4,c5,c6,c7]
		E = Eleicoes("Bitslandia")
		for i in cs:
			E.adicionarCandidato(i)

		print(E.em_ordem())
		assert E.em_ordem()=='30000,40000,45000,50000,55000,60000,65000'


	except Exception as a:
		return traduzMensagem(a)
	return 'OK'


def teste11():
	try:
		c1 = Candidato("A",50000,550)
		c2 = Candidato("B",40000,31743)
		c3 = Candidato("C",60000,1343)
		c4 = Candidato("D",30000,1943)
		c5 = Candidato("D",45000,43)
		c6 = Candidato("E",55000,17843)
		c7 = Candidato("F",65000,13)
		cs = [c1,c2,c3,c4,c5,c6,c7]
		E = Eleicoes("Bitslandia")
		for i in cs:
			E.adicionarCandidato(i)
		assert E.pre_ordem()=='50000,40000,30000,45000,60000,55000,65000'


	except Exception as a:
		return traduzMensagem(a)
	return 'OK'


def teste12():
	try:
		c1 = Candidato("A",50000,550)
		c2 = Candidato("B",40000,31743)
		c3 = Candidato("C",60000,1343)
		c4 = Candidato("D",30000,1943)
		c5 = Candidato("D",45000,43)
		c6 = Candidato("E",55000,17843)
		c7 = Candidato("F",65000,13)
		cs = [c1,c2,c3,c4,c5,c6,c7]
		E = Eleicoes("Bitslandia")
		for i in cs:
			E.adicionarCandidato(i)
		assert E.pos_ordem()=='30000,45000,40000,55000,65000,60000,50000'


	except Exception as a:
		return traduzMensagem(a)
	return 'OK'


def teste13():
	try:
		c1 = Candidato("A",50000,550)
		c2 = Candidato("B",40000,31743)
		c3 = Candidato("C",60000,1343)
		c4 = Candidato("D",30000,1943)
		c5 = Candidato("D",45000,43)
		c6 = Candidato("E",55000,17843)
		c7 = Candidato("F",65000,13)
		cs = [c1,c2,c3,c4,c5,c6,c7]
		E = Eleicoes("Bitslandia")
		for i in cs:
			E.adicionarCandidato(i)
		assert E.__str__()=='(((30000)40000(45000))50000((55000)60000(65000)))'
		
	except Exception as a:
		return traduzMensagem(a)
	return 'OK'


def teste14():
	try:
		c1 = Candidato("A",50000,550)
		c2 = Candidato("B",50000,31743)
		c3 = Candidato("C",60000,1343)
		c4 = Candidato("D",30000,1943)
		c5 = Candidato("D",45000,43)
		c6 = Candidato("E",55000,17843)
		c7 = Candidato("F",65000,13)
		cs = [c1,c2,c3,c4,c5,c6,c7]
		E = Eleicoes("Bitslandia")
		for i in cs:
			E.adicionarCandidato(i)
		assert c1.esquerda == c2
		
	except Exception as a:
		return traduzMensagem(a)
	return 'OK'


def teste15():
	try:
		c1 = Candidato("A",50000,550)
		c2 = Candidato("B",40000,31743)
		c3 = Candidato("C",60000,1343)
		c4 = Candidato("D",30000,1943)
		c5 = Candidato("D",45000,43)
		c6 = Candidato("E",55000,17843)
		c7 = Candidato("F",65000,13)
		cs = [c1,c2,c3,c4,c5,c6,c7]
		E = Eleicoes("Bitslandia")
		for i in cs:
			E.adicionarCandidato(i)
		assert E.busca(30000).nome == "D"
		
	except Exception as a:
		return traduzMensagem(a)
	return 'OK'
def teste16():
	try:
		c = geraCandidatos(2000)


		E = Eleicoes("Bitslandia")
		for i in c:
			E.adicionarCandidato(i)


	except Exception as a:
		return traduzMensagem(a)
	return 'OK'


def teste17(): 
	try:
		c = geraCandidatos(2000)


		E = Eleicoes("Bitslandia")
		for i in c:
			E.adicionarCandidato(i)


		assert E.contaCandidatos() == 2000


	except Exception as a:
		return traduzMensagem(a)
	return 'OK'


def teste18(): 
	try:
		c = geraCandidatos(2000)


		E = Eleicoes("Bitslandia")
		for i in c:
			E.adicionarCandidato(i)


		assert E.contaCandidatosRecursivo(E.raiz) == 2000


	except Exception as a:
		return traduzMensagem(a)
	return 'OK'


def teste19():
	try:
		arquivo = open('candidatos.txt').read().split('\n')
		c = [] 
		for i in arquivo:
			s = i.split(';')
			c.append(Candidato(s[0],int(s[1]),int(s[2])))


		E = Eleicoes("Bitslandia")
		for i in c:
			E.adicionarCandidato(i)


		assert E.contaCandidatosRecursivo(E.raiz) == 2000


	except Exception as a:
		return traduzMensagem(a)
	return 'OK'




testes = [globals()['teste%d' % i]() for i in range(1, 20)]
cobertura = sum(1 for r in testes if r == "OK")




for indice, teste in enumerate(testes):
	r = teste
	
	#if r != 'OK':# comente para mostrar as mensagens de erro
	#	r = 'X'  # comente para mostrar as mensagens de erro
	
	print('Teste %02d : %s' % (indice+1,r))
nota_prevista = (cobertura/len(testes))*10


print('Nota prevista: %.2f' % nota_prevista)