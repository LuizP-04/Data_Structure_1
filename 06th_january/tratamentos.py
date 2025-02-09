import re
import random
from candidato import Candidato


def traduzMensagem(m):
	if len(m.__str__()) == 0:
		return 'Teste nao passou'
	d = {'NoneType':'None','not':'nao','is':'e','defined':'definido','arguments':'argumento','argument':'argumento(s)','an':'um','got':'recebeu','unexpected':'inesperado','but':'mas','takes':'recebe','were':'foram','given':'dados','has':'tem', 'no':'nao','attribute':'atributo'}
	m = m.__str__()


	padrao = r'\b(' + '|'.join(re.escape(k) for k in d.keys()) + r')\b'   
	traducao = re.sub(padrao, lambda match: d[match.group(0)], m)
    
	traducao = traducao.split()
	i = 0
	while i < len(traducao):
		if traducao[i] == 'nao':
			traducao[i-1],traducao[i] = traducao[i],traducao[i-1]
		i += 1


	return ' '.join(traducao)




def geraNome(tamanho):


	v = 'aeiou'
	inicio = 'abcdefghijklmnopqrstuvxz'
	c = ['sc','sd','nh','rr','ss','ll','nd','mp','b','c','d','f','g','h','j','k','l','m','n','p','q','r','s','t','v','x','z']
	nome = inicio[random.randint(0,len(inicio)-1)]


	if nome in v:
		nome += c[random.randint(0,len(c)-1)]
	else:
		nome += v[random.randint(0,len(v)-1)]


	for i in range(tamanho-1):
		nome += v[random.randint(0,len(v)-1)]
		nome += c[random.randint(0,len(c)-1)]


	return nome


def geraCandidatos(numero):
	c = []


	
	try:
		for i in range(numero):
			c.append(Candidato(geraNome(5),random.randint(0,100000),random.randint(0,100000)))
	except:
		pass
	


	return c
