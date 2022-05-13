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