from candidato import Candidato
from concurso import Concurso


def teste0():

	try:
		n = Candidato('Joaquim',55)
	except:
		return 'X'
	return 'OK'

def teste1():

	try:
		n = Candidato('Joaquim',55)
		assert n.nome == 'Joaquim'
		assert n.nota == 55
	except:
		return 'X'
	return 'OK'

def teste2():

	try:
		n = Candidato('Joaquim',55)
		assert n.__str__() == '[Joaquim:55]'
	except:
		return 'X'
	return 'OK'


def teste3():

	try:
		c = Candidato('Joaquim',55)
		co = Concurso("Senado Federal")
	except:
		return 'X'
	return 'OK'

def teste4():

	try:
		c = Candidato('Joaquim',55)
		co = Concurso("Senado Federal")
		assert co.__str__() == 'Senado Federal[]'
	except:
		return 'X'
	return 'OK'

def teste5():

	try:
		c = Candidato('Joaquim',55)
		co = Concurso("Senado Federal")
		assert co.inscritos == 0
	except:
		return 'X'
	return 'OK'

def teste6():

	try:
		c = Candidato('Joaquim',55)
		co = Concurso("Senado Federal")
		co.inscrever(c)
	except:
		return 'X'
	return 'OK'

def teste7():

	try:
		c = Candidato('Joaquim',55)
		co = Concurso("Senado Federal")
		co.inscrever(c)
		assert co.inscritos == 1
	except:
		return 'X'
	return 'OK'

def teste8():

	try:
		c = Candidato('Joaquim',55)
		co = Concurso("Senado Federal")
		co.inscrever(c)
		assert co.primeiro_inscrito == c
	except:
		return 'X'
	return 'OK'

def teste9():

	try:
		c = Candidato('Joaquim',55)
		co = Concurso("Senado Federal")
		co.inscrever(c)
		assert co.primeiro_inscrito.anterior == c 
		assert co.primeiro_inscrito.posterior == c
	except:
		return 'X'
	return 'OK'

def teste10():

	try:
		c = Candidato('Joaquim',55)
		co = Concurso("Senado Federal")
		co.inscrever(c)
		assert co.__str__() == 'Senado Federal[Joaquim:55]'
	except:
		return 'X'
	return 'OK'

def teste11():

	try:
		c0 = Candidato('Rui Barbosa',80)
		c1 = Candidato("Machado de Assis",90)
		co = Concurso("Senado Federal")
		co.inscrever(c0)
		co.inscrever(c1)
		assert co.inscritos == 2
	except:
		return 'X'
	return 'OK'

def teste12():

	try:
		c0 = Candidato('Rui Barbosa',80)
		c1 = Candidato("Machado de Assis",90)
		co = Concurso("Senado Federal")
		co.inscrever(c0)
		co.inscrever(c1)
		assert c0.posterior.nome == 'Machado de Assis'
	except:
		return 'X'
	return 'OK'

def teste13():

	try:
		c0 = Candidato('Rui Barbosa',80)
		c1 = Candidato("Machado de Assis",90)
		co = Concurso("Senado Federal")
		co.inscrever(c0)
		co.inscrever(c1)
		assert c1.anterior.nome == 'Rui Barbosa'
	except:
		return 'X'
	return 'OK'

def teste14():

	try:
		c0 = Candidato('Rui Barbosa',80)
		c1 = Candidato("Machado de Assis",90)
		co = Concurso("Senado Federal")
		co.inscrever(c0)
		co.inscrever(c1)
		assert c0.posterior.posterior.nome == 'Rui Barbosa'
	except:
		return 'X'
	return 'OK'

def teste15():

	try:
		c0 = Candidato('Rui Barbosa',80)
		c1 = Candidato("Machado de Assis",90)
		co = Concurso("Senado Federal")
		co.inscrever(c0)
		co.inscrever(c1)
		assert c0.posterior.posterior.posterior.posterior.posterior.nome == 'Machado de Assis'
	except:
		return 'X'
	return 'OK'


def teste16():
	try:
		c0 = Candidato('Rui Barbosa',80)
		c1 = Candidato("Machado de Assis",90)
		co = Concurso("Senado Federal")
		co.inscrever(c0)
		co.inscrever(c1)
		assert co.__str__() == 'Senado Federal[Rui Barbosa:80][Machado de Assis:90]'
	except:
		return 'X'
	return 'OK'

def teste17():
	
	try:
		c0 = Candidato('Rui Barbosa',80)
		c1 = Candidato("Machado de Assis",90)
		c2 = Candidato("Cesar Lattes",85)
		co = Concurso("Senado Federal")
		co.inscrever(c0)
		co.inscrever(c1)
		co.inscrever(c2)
		assert co.__str__() == 'Senado Federal[Rui Barbosa:80][Machado de Assis:90][Cesar Lattes:85]'
	except:
		return "X"
	return "OK"""

def teste18():
	
	try:
		c0 = Candidato('Rui Barbosa',80)
		c1 = Candidato("Machado de Assis",90)
		c2 = Candidato("Cesar Lattes",85)
		co = Concurso("Senado Federal")
		co.inscrever(c0)
		co.inscrever(c1)
		co.inscrever(c2)
		assert c0.posterior.posterior.posterior.posterior.nome == 'Machado de Assis'
	except:
		return "X"
	return "OK"""

def teste19():
	
	try:
		
		co = Concurso("Senado Federal")
		assert co.busca('Euclides da Cunha') == None
	except:
		return "X"
	return "OK"

def teste20():
	
	try:
		c0 = Candidato('Rui Barbosa',80)
		co = Concurso("Senado Federal")
		co.inscrever(c0)
		assert co.busca('Rui Barbosa').nome == 'Rui Barbosa'
	except:
		return "X"
	return "OK"

def teste21():
	
	try:
		c0 = Candidato('Rui Barbosa',80)
		c1 = Candidato("Machado de Assis",90)
		co = Concurso("Senado Federal")
		co.inscrever(c0)
		co.inscrever(c1)
		assert co.busca('Machado de Assis').nome == 'Machado de Assis'
	except:
		return "X"
	return "OK"

def teste22():
	
	try:
		c0 = Candidato('Rui Barbosa',80)
		c1 = Candidato("Machado de Assis",90)
		co = Concurso("Senado Federal")
		co.inscrever(c0)
		co.inscrever(c1)
		assert co.busca('Euclides da Cunha') == None
	except:
		return "X"
	return "OK"

def teste23():
	
	try:
		c0 = Candidato('Rui Barbosa',80)
		co = Concurso("Senado Federal")
		co.inscrever(c0)
		assert co.remove('Rui Barbosa') == True
	except:
		return "X"
	return "OK"

def teste24():
	
	try:
		c0 = Candidato('Rui Barbosa',80)
		co = Concurso("Senado Federal")
		co.inscrever(c0)
		co.remove('Rui Barbosa')
		assert co.inscritos == 0
	except:
		return "X"
	return "OK"

def teste25():
	
	try:
		c0 = Candidato('Rui Barbosa',80)
		co = Concurso("Senado Federal")
		co.inscrever(c0)
		assert co.remove('Euclides da Cunha') == False
	except:
		return "X"
	return "OK"

def teste26():
	
	try:
		c0 = Candidato('Rui Barbosa',80)
		co = Concurso("Senado Federal")
		co.inscrever(c0)
		co.remove('Rui Barbosa')
		assert co.busca('Rui Barbosa') == None
	except:
		return "X"
	return "OK"

def teste27():
	
	try:
		c0 = Candidato('Rui Barbosa',80)
		c1 = Candidato("Machado de Assis",90)
		co = Concurso("Senado Federal")
		co.inscrever(c0)
		co.inscrever(c1)
		co.remove('Rui Barbosa')
		assert co.busca('Machado de Assis').nota == 90
	except:
		return "X"
	return "OK"

def teste28():
	
	try:
		c0 = Candidato('Rui Barbosa',80)
		c1 = Candidato("Machado de Assis",90)
		co = Concurso("Senado Federal")
		co.inscrever(c0)
		co.inscrever(c1)
		co.remove('Machado de Assis')
		assert co.busca('Machado de Assis') == None
		assert co.busca('Rui Barbosa').nota == 80
		assert co.inscritos == 1
	except:
		return "X"
	return "OK"

def teste29():
	
	try:
		c0 = Candidato('Rui Barbosa',80)
		c1 = Candidato("Machado de Assis",90)
		c2 = Candidato("Cesar Lattes",85)
		co = Concurso("Senado Federal")
		co.inscrever(c0)
		co.inscrever(c1)
		co.inscrever(c2)
		co.remove('Rui Barbosa')
		assert co.busca('Rui Barbosa') == None
		assert co.inscritos == 2
	except:
		return "X"
	return "OK"

def teste30():
	
	try:
		c0 = Candidato('Rui Barbosa',80)
		c1 = Candidato("Machado de Assis",90)
		c2 = Candidato("Cesar Lattes",85)
		co = Concurso("Senado Federal")
		co.inscrever(c0)
		co.inscrever(c1)
		co.inscrever(c2)
		co.remove('Machado de Assis')
		assert co.busca('Machado de Assis') == None
		assert co.inscritos == 2
	except:
		return "X"
	return "OK"

def teste31():
	
	try:
		c0 = Candidato('Rui Barbosa',80)
		c1 = Candidato("Machado de Assis",90)
		c2 = Candidato("Cesar Lattes",85)
		co = Concurso("Academia de Letras")
		co.inscrever(c0)
		co.inscrever(c1)
		co.inscrever(c2)
		co.remove('Machado de Assis')
		c3 = Candidato("Ariano Suassuna",70)
		co.inscrever(c3)
		assert co.__str__() == 'Academia de Letras[Rui Barbosa:80][Cesar Lattes:85][Ariano Suassuna:70]'
		co.remove('Rui Barbosa')
		assert co.__str__() == 'Academia de Letras[Cesar Lattes:85][Ariano Suassuna:70]'
		co.remove('Ariano Suassuna')
		assert co.__str__() == 'Academia de Letras[Cesar Lattes:85]'
		co.remove('Cesar Lattes')
		assert co.__str__() == 'Academia de Letras[]'
		assert co.inscritos == 0
	except:
		return "X"
	return "OK"

def teste32():
	try:
		c0 = Candidato('Rui Barbosa',80)
		c1 = Candidato("Machado de Assis",90)
		c2 = Candidato("Cesar Lattes",85)
		c3 = Candidato("Euclides da Cunha",80)
		co = Concurso("Senado Federal")
		co.inscrever(c0)
		co.inscrever(c1)
		co.inscrever(c2)
		co.inscrever(c3)
		assert co.candidatos() == ['Cesar Lattes', 'Euclides da Cunha', 'Machado de Assis', 'Rui Barbosa']
	except:
		return 'X'
	return 'OK'

def teste33():
	try:
		c0 = Candidato('Rui Barbosa',81)
		c1 = Candidato("Machado de Assis",91)
		c2 = Candidato("Cesar Lattes",81)
		c3 = Candidato("Euclides da Cunha",81)
		co = Concurso("Senado Federal")
		co.inscrever(c0)
		co.inscrever(c1)
		co.inscrever(c2)
		co.inscrever(c3)
		co.remove(pontuacao='Par')
		assert co.busca('Rui Barbosa').nome == 'Rui Barbosa'
	except:
		return 'X'
	return 'OK'

def teste34():
	try:
		c0 = Candidato('Rui Barbosa',82)
		c1 = Candidato("Machado de Assis",92)
		c2 = Candidato("Cesar Lattes",82)
		c3 = Candidato("Euclides da Cunha",82)
		co = Concurso("Senado Federal")
		co.inscrever(c0)
		co.inscrever(c1)
		co.inscrever(c2)
		co.inscrever(c3)
		co.remove(pontuacao='Impar')#nao remove nenhum candidato,pois nenhum tem nota impar
		assert co.busca('Rui Barbosa').nome == 'Rui Barbosa'
		assert co.inscritos == 4
	except:
		return 'X'
	return 'OK'

def teste35():
	try:
		c0 = Candidato('Rui Barbosa',81)
		c1 = Candidato("Machado de Assis",92)
		c2 = Candidato("Cesar Lattes",85)
		c3 = Candidato("Euclides da Cunha",82)
		co = Concurso("Senado Federal")
		co.inscrever(c0)
		co.inscrever(c1)
		co.inscrever(c2)
		co.inscrever(c3)
		co.remove(pontuacao='Impar') #remove Rui Barbosa, pois ele e o primeiro com nota impar
		assert co.candidatos() == ['Cesar Lattes', 'Euclides da Cunha', 'Machado de Assis']
		co.remove(pontuacao='Impar')#remove Cesar Lattes, pois ele e o proximo com nota impar
		assert co.candidatos() == ['Euclides da Cunha', 'Machado de Assis']
		co.remove(pontuacao='Par')
		assert co.candidatos() == ['Euclides da Cunha']
		co.remove(pontuacao='Impar')
		assert co.candidatos() == ['Euclides da Cunha']
		co.remove(pontuacao='Par')
		assert co.candidatos() == ['']

	except:
		return 'X'
	return 'OK'


testes = [teste0(),teste1(),teste2(),teste3(),teste4(),teste5(),teste6(),teste7(),
		  teste8(),teste9(),teste10(),teste11(),teste12(),teste13(),teste14(),
		  teste15(),teste16(),teste17(),teste18(),teste19(),teste20(),teste21(),
		  teste22(),teste23(),teste24(),teste25(),teste26(),teste27(),teste28(),
		  teste29(),teste30(),teste31(),teste32(),teste33(),teste34(),teste35()]
cobertura = 0
for indice, teste in enumerate(testes):
	r = teste
	if r == 'OK':
		cobertura += 1
	print('Teste %02d : %s' % (indice,r))

print('Cobertura Total: %.2f%%' % ((cobertura/len(testes)*100)))