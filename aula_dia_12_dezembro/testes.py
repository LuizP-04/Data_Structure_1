from paciente import Paciente
from upa import UPA 
from procedimentos import Exame
from procedimentos import Medicamento
from tratamentos import *

def teste1():

	try:
		p = Paciente('Joao')
	except Exception as a:
		return traduzMensagem(a)
	return 'OK'

def teste2():

	try:
		p = Paciente('Joao')
		assert p.criterio_risco == None
	except Exception as a:
		return traduzMensagem(a)
	return 'OK'

def teste3():

	try:
		p = Paciente('Joao')
		p.mudarCriterio('BAIXO')
	except Exception as a:
		return traduzMensagem(a)
	return 'OK'

def teste4():

	try:
		p = Paciente('Joao')
		p.mudarCriterio('BAIXO')
		assert p.criterio_risco == 'BAIXO'
	except Exception as a:
		return traduzMensagem(a)
	return 'OK'


def teste5():

	try:
		p = Paciente('Joao')
		p.mudarCriterio('BAIXO')
		assert p.__str__() == '[Joao:BAIXO]'
	except Exception as a:
		return traduzMensagem(a)

	return 'OK'

def teste6():

	try:
		p = Paciente('Joao')
		assert p.__str__() == '[Joao:NAO DEFINIDO]'
	except Exception as a:
		return traduzMensagem(a)
	return 'OK'

def teste7():

	try:
		p = Paciente('Joao')
		m1 = Medicamento('Dipirona')
	except Exception as a:
		return traduzMensagem(a)
	return 'OK'

def teste8():

	try:
		p = Paciente('Joao')
		m1 = Medicamento('Dipirona')
		assert p.procedimentos == []
	except Exception as a:
		return traduzMensagem(a)
	return 'OK'

def teste9():

	try:
		p = Paciente('Joao')
		m1 = Medicamento('Dipirona')
		p.agendarMedicacao(m1)
	except Exception as a:
		return traduzMensagem(a)
	return 'OK'


def teste10():

	try:
		p = Paciente('Joao')
		m1 = Medicamento('Dipirona')
		p.agendarMedicacao(m1)
		assert p.procedimentos == [m1]
	except Exception as a:
		return traduzMensagem(a)
	return 'OK'

def teste11():

	try:
		"""em POO em python quando passamos um atributo igualando a um valor
		em uma funcao,
		dizemos que esse atributo vai recever esse valor
		
		por exemplo
		
		def soma(a,b=1,c=2,d=3):
			return a+b+c+d

		print(soma(10)) --> resultado 16 pois a=10+b=1+c=2+d=3
		print(soma(20,c=30)) --> resultado 54 pois a=20+b=1+c=30+d=3
		print(soma(10,20,30)) --> resultado 63 pois a=10+b=20+c=30+d=3

		"""
		p = Paciente(nome='Joao',capacidade_procedimentos=10)
		m1 = Medicamento('Dipirona')
		p.agendarMedicacao(m1)
		assert p.capacidade_procedimentos == 10
	except Exception as a:
		return traduzMensagem(a)
	return 'OK'

def teste12():

	try:
		p = Paciente('Joao')
		#o valor default do atributo capacidade_procedimentos deve ser 5
		assert p.capacidade_procedimentos == 5
	except Exception as a:
		return traduzMensagem(a)
	return 'OK'

def teste13():

	try:
		p = Paciente('Joao')
		assert p.total_procedimentos == 0
	except Exception as a:
		return traduzMensagem(a)
	return 'OK'

def teste14():

	try:
		p = Paciente('Joao',5)
		m1 = Medicamento('Dipirona')
		p.agendarMedicacao(m1)
		assert p.total_procedimentos == 1
	except Exception as a:
		return traduzMensagem(a)
	return 'OK'

def teste15():

	try:
		p = Paciente('Joao',3)
		m1 = Medicamento('Dipirona')
		m2 = Medicamento('Buscopan')
		m3 = Medicamento('Ametalina')
		p.agendarMedicacao(m1)
		p.agendarMedicacao(m2)
		p.agendarMedicacao(m3)
		assert p.total_procedimentos == 3
	except Exception as a:
		return traduzMensagem(a)
	return 'OK'

def teste16():

	try:
		p = Paciente('Joao',3)
		m1 = Medicamento('Dipirona')
		m2 = Medicamento('Buscopan')
		m3 = Medicamento('Ametalina')
		p.agendarMedicacao(m1)
		p.agendarMedicacao(m2)
		p.agendarMedicacao(m3)
		assert p.procedimentos[0] == m1
		assert p.procedimentos[1] == m2
		assert p.procedimentos[2] == m3
	except Exception as a:
		return traduzMensagem(a)
	return 'OK'

def teste17():

	try:
		p = Paciente('Joao',3)
		m1 = Medicamento('Dipirona')
		m2 = Medicamento('Buscopan')
		m3 = Medicamento('Ametalina')
		p.agendarMedicacao(m1)
		p.agendarMedicacao(m2)
		p.agendarMedicacao(m3)
		p.executarProximoProcedimento()
	except Exception as a:
		return traduzMensagem(a)
	return 'OK'

def teste18():

	try:
		p = Paciente('Joao',3)
		m1 = Medicamento('Dipirona')
		m2 = Medicamento('Buscopan')
		m3 = Medicamento('Ametalina')
		p.agendarMedicacao(m1)
		p.agendarMedicacao(m2)
		p.agendarMedicacao(m3)
		#um procedimento, seja medicacao ou exame eh executado e finalizado
		p.executarProximoProcedimento()
		assert p.total_procedimentos == 2
	except Exception as a:
		return traduzMensagem(a)
	return 'OK'

def teste19():

	try:
		p = Paciente('Joao',3)
		m1 = Medicamento('Dipirona')
		m2 = Medicamento('Buscopan')
		m3 = Medicamento('Ametalina')
		p.agendarMedicacao(m1)
		p.agendarMedicacao(m2)
		p.agendarMedicacao(m3)
		p.executarProximoProcedimento()
		assert p.proximoProcedimento().nome == 'Buscopan'
	except Exception as a:
		return traduzMensagem(a)
	return 'OK'

def teste20():

	try:
		p = Paciente('Joao',3)
		m1 = Medicamento('Dipirona')
		m2 = Medicamento('Buscopan')
		m3 = Medicamento('Ametalina')
		p.agendarMedicacao(m1)
		p.agendarMedicacao(m2)
		p.agendarMedicacao(m3)
		p.executarProximoProcedimento()
		assert p.procedimentos == [m1,m2]
	except Exception as a:
		return traduzMensagem(a)
	return 'OK'

def teste21():

	try:
		p = Paciente('Joao',3)
		m1 = Medicamento('Dipirona')
		m2 = Medicamento('Buscopan')
		m3 = Medicamento('Ametalina')
		m4 = Medicamento('Toricanol')
		p.agendarMedicacao(m1)
		p.agendarMedicacao(m2)
		p.agendarMedicacao(m3)
		p.agendarMedicacao(m4)
		assert p.total_procedimentos == 4
		assert p.proximoProcedimento().nome == m4.nome
	except Exception as a:
		return traduzMensagem(a)
	return 'OK'

def teste22():

	try:
		p = Paciente('Joao',3)
		m1 = Medicamento('Dipirona')
		m2 = Medicamento('Buscopan')
		e1 = Exame('Raio-X')
		p.agendarMedicacao(m1)
		p.agendarMedicacao(m2)
		p.agendarExame(e1)
		assert p.total_procedimentos == 3
		assert p.proximoProcedimento().nome == e1.nome
	except Exception as a:
		return traduzMensagem(a)
	return 'OK'

def teste23():

	try:
		p = Paciente('Joao',3)
		m1 = Medicamento('Dipirona')
		m2 = Medicamento('Buscopan')
		e1 = Exame('Raio-X')
		p.agendarMedicacao(m1)
		p.agendarMedicacao(m2)
		p.agendarExame(e1)
		assert p.listarProcedimentos() == 'Dipirona,Buscopan,Raio-X'
	except Exception as a:
		return traduzMensagem(a)
	return 'OK'

def teste24():

	try:
		p = Paciente('Joao',3)
		m1 = Medicamento('Dipirona')
		m2 = Medicamento('Buscopan')
		e1 = Exame('Raio-X')
		p.agendarMedicacao(m1)
		p.agendarMedicacao(m2)
		p.agendarExame(e1)
		assert p.foi_atendido == True
	except Exception as a:
		return traduzMensagem(a)
	return 'OK'

def teste25():

	try:
		p = Paciente('Joao',3)
		m1 = Medicamento('Dipirona')
		m2 = Medicamento('Buscopan')
		e1 = Exame('Raio-X')
		assert p.foi_atendido == False
	except Exception as a:
		return traduzMensagem(a)
	return 'OK'

def teste26():

	try:
		p = Paciente('Joao',3)
		m1 = Medicamento('Dipirona')
		m2 = Medicamento('Buscopan')
		e1 = Exame('Raio-X')
		p.agendarMedicacao(m1)
		p.agendarMedicacao(m2)
		p.agendarExame(e1)
		p.executarProximoProcedimento()
		p.executarProximoProcedimento()
		p.executarProximoProcedimento()
		assert p.estaLiberado() == True
	except Exception as a:
		return traduzMensagem(a)
	return 'OK'

def teste27():

	try:
		p = Paciente('Joao',3)
		m1 = Medicamento('Dipirona')
		m2 = Medicamento('Buscopan')
		e1 = Exame('Raio-X')
		p.agendarMedicacao(m1)
		p.agendarMedicacao(m2)
		p.agendarExame(e1)
		assert p.estaLiberado() == False
	except Exception as a:
		return traduzMensagem(a)
	return 'OK'

def teste28():

	try:
		p = Paciente('Joao',3)
		m1 = Medicamento('Dipirona')
		m2 = Medicamento('Buscopan')
		e1 = Exame('Raio-X')
		assert p.estaLiberado() == False
	except Exception as a:
		return traduzMensagem(a)
	return 'OK'
def teste29():

	try:
		upa1 = UPA('Parintins')
	except Exception as a:
		return traduzMensagem(a)
	return 'OK'

def teste30():

	try:
		upa1 = UPA('Parintins')
		p = Paciente('Joao')
		upa1.incluirPacienteNaFilaDeEspera(p)
	except Exception as a:
		return traduzMensagem(a)
	return 'OK'

def teste31():

	try:
		upa1 = UPA('Parintins')
		p = Paciente('Joao')
		assert upa1.tamanhoFilaEspera == 0

	except Exception as a:
		return traduzMensagem(a)
	return 'OK'

def teste32():

	try:
		upa1 = UPA('Parintins')
		p = Paciente('Joao')
		upa1.incluirPacienteNaFilaDeEspera(p)
		#so pode incluir na fila se o paciente tiver passado pela
		#classificao de risco

		assert upa1.tamanhoFilaEspera == 0

	except Exception as a:
		return traduzMensagem(a)
	return 'OK'

def teste33():

	try:
		upa1 = UPA('Parintins')
		p1 = Paciente('Joao')
		p1.mudarCriterio('BAIXO')
		p2 = Paciente('Ana')
		p2.mudarCriterio('ALTO')
		upa1.incluirPacienteNaFilaDeEspera(p1)
		upa1.incluirPacienteNaFilaDeEspera(p2)
		assert upa1.tamanhoFilaEspera == 2
	except Exception as a:
		return traduzMensagem(a)
	return 'OK'

def teste34():

	try:
		upa1 = UPA('Parintins')
		p1 = Paciente('Joao')
		p1.mudarCriterio('BAIXO')
		p2 = Paciente('Ana')
		p2.mudarCriterio('BAIXO')
		upa1.incluirPacienteNaFilaDeEspera(p1)
		upa1.incluirPacienteNaFilaDeEspera(p2)
		assert p1.paciente_posterior.nome == p2.nome
		assert p2.paciente_anterior.nome == p1.nome
	except Exception as a:
		return traduzMensagem(a)
	return 'OK'

def teste35():

	try:
		upa1 = UPA('Parintins')
		p1 = Paciente('Joao')
		p1.mudarCriterio('BAIXO')
		p2 = Paciente('Ana')
		p2.mudarCriterio('ALTO')
		p3 = Paciente('Beatriz')
		p3.mudarCriterio('BAIXO')
		upa1.incluirPacienteNaFilaDeEspera(p1)
		upa1.incluirPacienteNaFilaDeEspera(p2)
		upa1.incluirPacienteNaFilaDeEspera(p3)
		assert p1.paciente_posterior.paciente_posterior == p3
		assert p3.paciente_anterior.paciente_anterior == p1
	except Exception as a:
		return traduzMensagem(a)
	return 'OK'

def teste36():

	try:
		upa1 = UPA('Parintins')
		p1 = Paciente('Joao')
		p1.mudarCriterio('BAIXO')
		p2 = Paciente('Ana')
		p3 = Paciente('Beatriz')
		p3.mudarCriterio('BAIXO')
		upa1.incluirPacienteNaFilaDeEspera(p1)
		upa1.incluirPacienteNaFilaDeEspera(p2)
		upa1.incluirPacienteNaFilaDeEspera(p3)
		assert p1.paciente_posterior.paciente_posterior == None
	except Exception as a:
		return traduzMensagem(a)
	return 'OK'

def teste37():

	try:
		upa1 = UPA('Parintins')
		p1 = Paciente('Joao')
		p1.mudarCriterio('BAIXO')
		p2 = Paciente('Ana')
		p2.mudarCriterio('ALTO')
		p3 = Paciente('Beatriz')
		p3.mudarCriterio('BAIXO')
		upa1.incluirPacienteNaFilaDeEspera(p1)
		upa1.incluirPacienteNaFilaDeEspera(p2)
		upa1.incluirPacienteNaFilaDeEspera(p3)
		assert upa1.chamarPaciente().nome == 'Ana'
	except Exception as a:
		return traduzMensagem(a)
	return 'OK'

def teste38():

	try:
		upa1 = UPA('Parintins')
		p1 = Paciente('Joao')
		p1.mudarCriterio('ALTO')
		p2 = Paciente('Ana')
		p2.mudarCriterio('ALTO')
		p3 = Paciente('Beatriz')
		p3.mudarCriterio('ALTO')
		upa1.incluirPacienteNaFilaDeEspera(p1)
		upa1.incluirPacienteNaFilaDeEspera(p2)
		upa1.incluirPacienteNaFilaDeEspera(p3)
		assert upa1.chamarPaciente().nome == 'Joao'
	except Exception as a:
		return traduzMensagem(a)
	return 'OK'

def teste39():

	try:
		upa1 = UPA('Parintins')
		p1 = Paciente('Joao')
		p1.mudarCriterio('BAIXO')
		p2 = Paciente('Ana')
		p2.mudarCriterio('BAIXO')
		p3 = Paciente('Beatriz')
		p3.mudarCriterio('BAIXO')
		upa1.incluirPacienteNaFilaDeEspera(p1)
		upa1.incluirPacienteNaFilaDeEspera(p2)
		upa1.incluirPacienteNaFilaDeEspera(p3)
		assert upa1.chamarPaciente().nome == 'Joao'
	except Exception as a:
		return traduzMensagem(a)
	return 'OK'

def teste40():

	try:
		upa1 = UPA('Parintins')
		p1 = Paciente('Joao')
		p1.mudarCriterio('ALTO')
		p2 = Paciente('Ana')
		p2.mudarCriterio('BAIXO')
		p3 = Paciente('Beatriz')
		p3.mudarCriterio('ALTO')
		upa1.incluirPacienteNaFilaDeEspera(p1)
		upa1.incluirPacienteNaFilaDeEspera(p2)
		upa1.incluirPacienteNaFilaDeEspera(p3)
		assert upa1.chamarPaciente().nome == 'Joao'
	except Exception as a:
		return traduzMensagem(a)
	return 'OK'

def teste41():

	try:
		upa1 = UPA('Parintins')
		p1 = Paciente('Joao')
		p1.mudarCriterio('ALTO')
		p2 = Paciente('Ana')
		p2.mudarCriterio('BAIXO')
		p3 = Paciente('Beatriz')
		p3.mudarCriterio('ALTO')
		upa1.incluirPacienteNaFilaDeEspera(p1)
		upa1.incluirPacienteNaFilaDeEspera(p2)
		upa1.incluirPacienteNaFilaDeEspera(p3)
		upa1.chamarPaciente()
		assert upa1.tamanhoFilaEspera == 2
	except Exception as a:
		return traduzMensagem(a)
	return 'OK'

def teste42():

	try:
		upa1 = UPA('Parintins')
		p1 = Paciente('Joao')
		p1.mudarCriterio('BAIXO')
		p2 = Paciente('Ana')
		p2.mudarCriterio('BAIXO')
		p3 = Paciente('Beatriz')
		p3.mudarCriterio('ALTO')
		upa1.incluirPacienteNaFilaDeEspera(p1)
		upa1.incluirPacienteNaFilaDeEspera(p2)
		upa1.incluirPacienteNaFilaDeEspera(p3)
		assert upa1.chamarPaciente().nome=='Beatriz'
	except Exception as a:
		return traduzMensagem(a)
	return 'OK'

def teste43():

	try:
		upa1 = UPA('Parintins')
		p1 = Paciente('Joao')
		p1.mudarCriterio('BAIXO')
		upa1.incluirPacienteNaFilaDeEspera(p1)
		upa1.chamarPaciente()
	except Exception as a:
		return traduzMensagem(a)
	return 'OK'

def teste44():

	try:
		upa1 = UPA('Parintins')
		p1 = Paciente('Joao')
		p1.mudarCriterio('ALTO')
		p2 = Paciente('Ana')
		p2.mudarCriterio('BAIXO')
		p3 = Paciente('Beatriz')
		p3.mudarCriterio('ALTO')
		upa1.incluirPacienteNaFilaDeEspera(p1)
		upa1.incluirPacienteNaFilaDeEspera(p2)
		upa1.incluirPacienteNaFilaDeEspera(p3)
		upa1.chamarPaciente()
		assert p2.paciente_anterior == None
		assert p1.paciente_posterior == None
	except Exception as a:
		return traduzMensagem(a)
	return 'OK'

def teste45():

	try:
		upa1 = UPA('Parintins')
		p1 = Paciente('Joao')
		p1.mudarCriterio('BAIXO')
		p2 = Paciente('Ana')
		p2.mudarCriterio('BAIXO')
		p3 = Paciente('Beatriz')
		p3.mudarCriterio('ALTO')
		upa1.incluirPacienteNaFilaDeEspera(p1)
		upa1.incluirPacienteNaFilaDeEspera(p2)
		upa1.incluirPacienteNaFilaDeEspera(p3)
		upa1.chamarPaciente()
		assert p3.paciente_anterior == None
		assert p2.paciente_posterior == None
	except Exception as a:
		return traduzMensagem(a)
	return 'OK'



def teste46():

	try:
		upa1 = UPA('Parintins')
		p1 = Paciente('Joao')
		p1.mudarCriterio('BAIXO')
		p2 = Paciente('Ana')
		p2.mudarCriterio('ALTO')
		p3 = Paciente('Beatriz')
		p3.mudarCriterio('ALTO')
		p4 = Paciente('Joaquim')
		p4.mudarCriterio('MEDIO')
		upa1.incluirPacienteNaFilaDeEspera(p1)
		upa1.incluirPacienteNaFilaDeEspera(p2)
		upa1.incluirPacienteNaFilaDeEspera(p3)
		upa1.incluirPacienteNaFilaDeEspera(p4)
		upa1.chamarPaciente()
		assert p1.paciente_posterior.paciente_posterior.nome == 'Joaquim'
		assert p4.paciente_anterior.paciente_anterior.nome == 'Joao'
	except Exception as a:
		return traduzMensagem(a)
	return 'OK'

def teste47():

	try:
		upa1 = UPA('Parintins')
		p1 = Paciente('Joao')
		p1.mudarCriterio('BAIXO')
		p2 = Paciente('Ana')
		p2.mudarCriterio('ALTO')
		p3 = Paciente('Beatriz')
		p3.mudarCriterio('ALTO')
		p4 = Paciente('Joaquim')
		p4.mudarCriterio('MEDIO')
		upa1.incluirPacienteNaFilaDeEspera(p1)
		upa1.incluirPacienteNaFilaDeEspera(p2)
		upa1.incluirPacienteNaFilaDeEspera(p3)
		upa1.incluirPacienteNaFilaDeEspera(p4)
		upa1.chamarPaciente()
		upa1.chamarPaciente()
		upa1.chamarPaciente()
		upa1.chamarPaciente()
		assert upa1.tamanhoFilaEspera == 0
	except Exception as a:
		return traduzMensagem(a)
	return 'OK'


def teste48():

	try:
		upa1 = UPA('Parintins')
		p1 = Paciente('Joao')
		p1.mudarCriterio('BAIXO')
		p2 = Paciente('Ana')
		p2.mudarCriterio('ALTO')
		p3 = Paciente('Beatriz')
		p3.mudarCriterio('ALTO')
		p4 = Paciente('Joaquim')
		p4.mudarCriterio('MEDIO')
		upa1.incluirPacienteNaFilaDeEspera(p1)
		upa1.incluirPacienteNaFilaDeEspera(p2)
		upa1.incluirPacienteNaFilaDeEspera(p3)
		upa1.incluirPacienteNaFilaDeEspera(p4)
		assert upa1.__str__() == '[Joao:BAIXO][Ana:ALTO][Beatriz:ALTO][Joaquim:MEDIO]'
	except Exception as a:
		return traduzMensagem(a)
	return 'OK'

def teste49():

	try:
		upa1 = UPA('Parintins')
		assert upa1.__str__() == '[]'
	except Exception as a:
		return traduzMensagem(a)
	return 'OK'

def teste50():

	try:
		upa1 = UPA('Parintins')
		pacientes = [Paciente(geraNome()) for i in range(50)]
		criterios = ['BAIXO','ALTO','MEDIO','URGENTE']
		[p.mudarCriterio(criterios[random.randint(0,3)]) for p in pacientes]
		[upa1.incluirPacienteNaFilaDeEspera(p) for p in pacientes]
		[upa1.chamarPaciente() for i in range(50)]
		assert upa1.tamanhoFilaEspera == 0
		assert upa1.__str__() == '[]'
	except Exception as a:
		return traduzMensagem(a)
	return 'OK'



testes = [globals()['teste%d' % i]() for i in range(1, 51)]
cobertura = sum(1 for r in testes if r == "OK")


for indice, teste in enumerate(testes):
	r = teste
	
	"""if r != 'OK':# comente para mostrar as mensagens de erro
		r = 'X'  # comente para mostrar as mensagens de erro
	"""
	print('Teste %02d : %s' % (indice+1,r))
print('Cobertura Total: %.2f%%' % ((cobertura/len(testes)*100)))