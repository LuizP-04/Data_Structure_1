import re
import random
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


def geraMedicamento():
    pref = ["xilo", "para", "cloro", "benzo", "dexa", "metro", "sulfa", "cipro", "fluo"]
    inf = ["cain", "fen", "nidr", "praz", "morf", "cet", "pril", "zol"]
    suf = ["ina", "ano", "eno", "ona", "ilo", "ina", "ida", "ol", "am"]


  
    prefixo = random.choice(pref)
    infixo = random.choice(inf)
    suffixo = random.choice(suf)




    return '%s%s%s' % (prefixo,infixo,suffixo)


def geraNome():


	c = 'bcdfghjklmnpqrstvxz'
	v = 'aeiou'


	return ''.join([c[random.randint(0,len(c)-1)]+v[random.randint(0,len(v)-1)] for i in range(random.randint(3,10))])


[1 for i in range(50)]
