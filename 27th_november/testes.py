from competidor import Competidor
from ranking import Ranking


def teste0():

	try:
		c = Competidor('Turing')
	except:
		return 'X'

	return 'OK'

def teste1():

	try:
		c = Competidor('Turing')
		assert c.esquerda == c.direita
	except:
		return 'X'

	return 'OK'

def teste2():

	try:
		c = Competidor('Turing')
		assert c.pontuacao == 0
	except:
		return 'X'

	return 'OK'

def teste3():

	try:
		c = Competidor('Turing')
		c.alterarPontuacao(20)
		assert c.pontuacao == 20
	except:
		return 'X'

	return 'OK'

def teste4():

	try:
		c = Competidor('Turing')
		c.alterarPontuacao(20)
		c.alterarPontuacao(-5)
		assert c.pontuacao == 15
	except:
		return 'X'

	return 'OK'

def teste5():

	try:
		c = Competidor('Turing')
		assert c.__str__() == '[Turing:0]'
	except:
		return 'X'

	return 'OK'

def teste6():

	try:
		R = Ranking()
	except:
		return 'X'

	return 'OK'

def teste7():

	
	try:
		R = Ranking()
		c = Competidor("Turing")
		R.inserir(c)
		assert R.total_competidores == 1
	except:
		return 'X'

	return 'OK'

def teste8():

	
	try:
		R = Ranking()
		c = Competidor("Turing")
		c.alterarPontuacao(200)
		c2 = Competidor("Knuth")
		c2.alterarPontuacao(150)
		R.inserir(c)
		R.inserir(c2)
		assert R.total_competidores == 2
	except:
		return 'X'

	return 'OK'

def teste9():
	
	try:
		R = Ranking()
		c = Competidor("Turing")
		c.alterarPontuacao(200)
		c2 = Competidor("Knuth")
		c2.alterarPontuacao(300)
		R.inserir(c)
		R.inserir(c2)
		assert R.__str__() == '[Knuth:300][Turing:200]'
	except:
		return 'X'

	return 'OK'

def teste10():
	
	try:
		R = Ranking()
		c = Competidor("Turing")
		c.alterarPontuacao(200)
		c2 = Competidor("Knuth")
		c2.alterarPontuacao(300)
		c3 = Competidor('LeCun')
		c3.alterarPontuacao(250)
		R.inserir(c)
		R.inserir(c2)
		R.inserir(c3)
		assert R.total_competidores == 3
		assert R.__str__() == '[Knuth:300][LeCun:250][Turing:200]'
	except:
		return 'X'

	return 'OK'

def teste11():
	
	try:
		R = Ranking()
		c = Competidor("Turing")
		c.alterarPontuacao(200)
		c2 = Competidor("Knuth")
		c2.alterarPontuacao(300)
		c3 = Competidor('LeCun')
		c3.alterarPontuacao(250)
		c4 = Competidor("Bagio")
		c4.alterarPontuacao(263)
		c5 = Competidor("Tourist")
		c5.alterarPontuacao(3998)
		c6 = Competidor("Manaus")
		c6.alterarPontuacao(53)
		R.inserir(c)
		R.inserir(c2)
		R.inserir(c3)
		R.inserir(c4)
		R.inserir(c5)
		R.inserir(c6)
		assert R.total_competidores == 6
		assert R.__str__() == '[Tourist:3998][Knuth:300][Bagio:263][LeCun:250][Turing:200][Manaus:53]'
	except:
		return 'X'

	return 'OK'

def teste12():
	
	try:
		R = Ranking()
		c = Competidor("Turing",200)
		c2 = Competidor("Knuth",300)
		c3 = Competidor('LeCun',250)
		c4 = Competidor("Bagio",263)
		c5 = Competidor("Tourist",3998)
		c6 = Competidor("Manaus",53)
		R.inserir(c)
		R.inserir(c2)
		R.inserir(c3)
		R.inserir(c4)
		R.inserir(c5)
		R.inserir(c6)
		assert R.total_competidores == 6
		assert R.__str__() == '[Tourist:3998][Knuth:300][Bagio:263][LeCun:250][Turing:200][Manaus:53]'
	except:
		return 'X'

	return 'OK'

def teste13():
	
	try:
		R = Ranking()
		c = Competidor("Turing",200)
		c2 = Competidor("Knuth",300)
		c3 = Competidor('LeCun',250)
		c4 = Competidor("Bagio",263)
		c5 = Competidor("Tourist",3998)
		c6 = Competidor("Manaus",53)
		R.inserir(c)
		R.inserir(c2)
		R.inserir(c3)
		R.inserir(c4)
		R.inserir(c5)
		R.inserir(c6)

		assert R.busca('Bagio').nome == 'Bagio'
		
	except:
		return 'X'

	return 'OK'

def teste14():
	
	try:
		R = Ranking()
		c = Competidor("Turing",200)
		c2 = Competidor("Knuth",300)
		c3 = Competidor('LeCun',250)
		c4 = Competidor("Bagio",263)
		c5 = Competidor("Tourist",3998)
		c6 = Competidor("Manaus",53)
		R.inserir(c)
		R.inserir(c2)
		R.inserir(c3)
		R.inserir(c4)
		R.inserir(c5)
		R.inserir(c6)

		assert R.busca('Titanic') == None
		
	except:
		return 'X'

	return 'OK'

def teste15():
	
	try:
		R = Ranking()
		c = Competidor("Turing",200)
		R.inserir(c)
		print(R.total_competidores)
		assert R.remover('Turing') == True
		assert R.total_competidores == 0
		assert R.__str__() == '[]'
		assert R.busca('Turing') == None
		
	except:
		return 'X'

	return 'OK'

def teste16():
	
	try:
		R = Ranking()
		c = Competidor("Turing",200)
		c2 = Competidor("Knuth",300)
		R.inserir(c)
		R.inserir(c2)
		assert R.remover('Turing') == True
		assert R.total_competidores == 1
		assert R.__str__() == '[Knuth:300]'
		assert R.busca('Turing') == None
		
	except:
		return 'X'

	return 'OK'

def teste17():
	
	try:
		R = Ranking()
		c = Competidor("Turing",200)
		c2 = Competidor("Knuth",300)
		c3 = Competidor('LeCun',250)
		c4 = Competidor("Bagio",263)
		c5 = Competidor("Tourist",3998)
		c6 = Competidor("Manaus",53)
		R.inserir(c)
		R.inserir(c2)
		R.inserir(c3)
		R.inserir(c4)
		R.inserir(c5)
		R.inserir(c6)
		assert R.remover('LeCun') == True
		assert R.total_competidores == 5
		assert R.__str__() == '[Tourist:3998][Knuth:300][Bagio:263][Turing:200][Manaus:53]'
		assert R.busca('LeCun') == None
		
	except:
		return 'X'

	return 'OK'

def teste18():
	
	try:
		R = Ranking()
		c = Competidor("Turing",200)
		c2 = Competidor("Knuth",300)
		c3 = Competidor('LeCun',250)
		c4 = Competidor("Bagio",263)
		c5 = Competidor("Tourist",3998)
		c6 = Competidor("Manaus",53)
		R.inserir(c)
		R.inserir(c2)
		R.inserir(c3)
		R.inserir(c4)
		R.inserir(c5)
		R.inserir(c6)
		b = R.busca('LeCun')
		assert R.remover('LeCun') == True
		assert b.direita == b.esquerda
		
	except:
		return 'X'

	return 'OK'

testes = [teste0(),teste1(),teste2(),teste3(),teste4(),teste5(),
		  teste6(),teste7(),teste8(),teste9(),teste10(),teste11(),
		  teste12(),teste13(),teste14(),teste15(),teste16(),teste17(),
		  teste18()]
#,teste1(),teste2(),teste3(),teste4(),
#teste5(),teste6(),teste7(),teste8(),teste9(),
#teste10(),teste11(),teste12(),teste13()]"""


cobertura = 0
for indice, teste in enumerate(testes):
	r = teste
	if r == 'OK':
		cobertura += 1
	print('Teste %d : %s' % (indice,r))

print('Cobertura Total: %.2f%%' % ((cobertura/len(testes)*100)))