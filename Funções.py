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