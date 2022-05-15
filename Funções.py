import random as r

#Normalizando bases de países
def normaliza(dicio):
    dicio2 = {}
    for e,values in dicio.items(): 
        cont = {'continente': e}
        for e2,values2 in values.items():
            values2.update(cont)
            dicio2[e2]=values2
    return dicio2

#Sorteando Países
def sorteia_pais(dicio):
    lista = list(dicio.keys())
    b = r.choice(lista)
    return b

#Distância de Haversine
import math
def haversine(raio, lat1, lon1, lat2, lon2): 
    lat1 = lat1 * math.pi / 180 
    lon1 = lon1 * math.pi / 180 
    lat2 = lat2 * math.pi / 180 
    lon2 = lon2 * math.pi / 180 
    dlat = lat2 - lat1 
    dlon = lon2 - lon1 
    a = math.sin(dlat / 2) ** 2 + math.cos(lat1) * math.cos(lat2) * math.sin(dlon / 2) ** 2 
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a)) 
    d = raio * c 
    return d

#se está na lista
def esta_na_lista(pais,lista2):
    lista3 = []
    a = True
    for lista in lista2:       
        lista3.append(lista[0])
    if pais not in lista3:
        a = False
  
    return a

#adiciona pais e distancia se n existir
def adiciona_em_ordem(pais,dist,lista):
    lista2 = []
    p = [pais, dist]
    if pais in lista:
        return lista
    else:
        if len(lista) > 0:
            for e in lista:
                if dist < e[1] and p not in lista2:
                    lista2.append(p)
                    lista2.append(e)
                else:
                    lista2.append(e)
            if p not in lista2:
                lista2.append(p)
        else:
            lista2.append(p)
        return lista2

#sorteia letra
import random

def sorteia_letra(palavra, lista):
    r2 = ['.', ',', '-', ';', ' ']
    r1 = []
    for e in lista:
        if e >= 'a' and e <= 'z' or e >='A' and e <= 'Z':
            a = e.swapcase()
            r1.append(a)
            r1.append(e)
        else:
            r1.append(e)
    k = True
    soma = 0
    for e in palavra:
        if e not in r1 and e not in r2:
            soma += 1
    if soma > 0:
        while k:
            sorteada = random.choice(palavra)
            if sorteada not in r1 and sorteada not in r2:
                return sorteada
    else:
        return ''

def mercado_dicas(choices, lista_dicas_usadas):
    dicas_possiveis = [0,1,2,3,4,5]
    dicas_nao_usadas = []
    for dica in dicas_possiveis:
        if dica not in lista_dicas_usadas:
            dicas_nao_usadas.append(dica)
    dicas = '['

    for dica in dicas_nao_usadas:
        dicastr = str(dica)
        dicas += dicastr + '|'
    dicas += ']'

    md = 'Mercado de Dicas' + '\n'
    t1 = '----------------------------------------' + '\n'
    d1 = '1. Cor da bandeira  - custa 4 tentativas' + '\n'
    d2 = '2. Letra da capital - custa 3 tentativas' + '\n'
    d3 = '3. Área             - custa 6 tentativas' + '\n'
    d4 = '4. População        - custa 5 tentativas' + '\n'
    d5 = '5. Continente       - custa 7 tentativas' + '\n'
    d6 = '0. Sem dicas' + '\n'
    t2 = '----------------------------------------' + '\n'
    e1 = 'Escolha sua opção {0}'.format(dicas)

    if len(lista_dicas_usadas) == 0:
        a = md + t1 + d1 + d2 + d3 + d4 + d5 + d6 + t2 + e1
        return a
    
    para_print = md + t1

    if 1 in dicas_nao_usadas and choices >= 4:
        para_print += d1
    if 2 in dicas_nao_usadas and choices >= 3:
        para_print += d2
    if 3 in dicas_nao_usadas and choices >= 6:
        para_print += d3
    if 4 in dicas_nao_usadas and choices >= 5:
        para_print += d4
    if 5 in dicas_nao_usadas and choices >= 7:
        para_print += d5
        
    para_print += d6 + t2 + e1

    sem_dicas = md + t1 + d6 + t2 + e1 + '>>> Infelizmente, acabou seu estoque de dicas! <<<'
    
    if choices < 3:
        return sem_dicas
    else:
        return para_print

def func_dicas(lista_distancias, lista_dicas_usadas2, cor_bandeira, letra, area, populacao, continente):
    print_dist = '\n' + 'Distâncias:'
    print_dicas = '\n' + '\n' + 'Dicas:\n'      

    if 1 in lista_dicas_usadas2:
        print_dicas += '    - Cores da Bandeira: '
        for cor in cor_bandeira:
            if cor != cor_bandeira[-1]:
                print_dicas += cor + ', '
            else:
                print_dicas += cor + '\n'
    if 2 in lista_dicas_usadas2:
        print_dicas += '    - Letras da Capital: ' + letra + '\n'
    if 3 in lista_dicas_usadas2:
        print_dicas += '    - Área: ' + str(area) + ' km2' + '\n'
    if 4 in lista_dicas_usadas2:
        print_dicas += '    - População: ' + str(populacao) + ' habitantes' + '\n'
    if 5 in lista_dicas_usadas2:
        print_dicas += '    - Continente: ' + continente + '\n'
    
    for e in lista_distancias:
        
        if e[1] >= 1e4:
            print_dist += '\n' + '  {0}{1}{3} km -> {2}'.format('\033[4;30m',e[1],e[0],'\033[m')
        if 1e4 > e[1] >= 5000:
            print_dist += '\n' + '  {0}{1}{3} km -> {2}'.format('\033[4;35m',e[1],e[0],'\033[m')
        if 5000> e[1] >= 2000:
            print_dist += '\n' + '  {0}{1}{3} km -> {2}'.format('\033[4;31m',e[1],e[0],'\033[m')
        if e[1] < 2000:
            print_dist += '\n' + '  {0}{1}{3} km -> {2}'.format('\033[4;33m',e[1],e[0],'\033[m')
    para_print = print_dist + print_dicas
    return para_print