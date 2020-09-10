'''
Created on Jun 20, 2017
@author: vStojan
'''
import os
from htmlParser import Parser
from Trie import Trie
from Vertex import Graph
import pickle
from bucketSort import Item
from rest.bucketSort import bucket_sort
  
def pronadji_ucitaj_fajlove(path,list):
    if not os.path.isdir(path):
        pass
    else:
        files = os.listdir(path)
        for filename in files:
            pronadji_ucitaj_fajlove(os.path.join(path, filename),list)
            if filename.endswith(".html"):
                list.append(os.path.join(path, filename))

def napuni_traj(lista,traj,g): 
    p = Parser()
    for l in lista:
        p.parse(l)
        cvor = g.insert_vertex(l)     
        for rec in p.words:
            rec1 = rec.lower()
            traj.add(rec1, l)
        for link in p.links:
            v = g.insert_vertex(link)
            g.instert_edge(cvor, v, 1)
def bablesort(lista):
    for l in range(len(lista)-1,-1,-1):
        for j in range(l):
            if lista[l].values()[0] > lista[j].values()[0]:
                lista[l],lista[j] = lista[j],lista[l]
            
def rangiranje(listaLinkova):
    for link in listaLinkova:
        brojac_za_reci = 0
        brojac_za_graf = 0
        brojac_za_linkove = 0
        brojac_za_reci +=  listaLinkova[link]
        brojac_za_graf += g.degree(g._linkovi[link], True)
        recnik_dolaznih_Linkova = g._incoming[g._linkovi[link]]
        for reci in recnik_dolaznih_Linkova:
            if reci._element in listaLinkova:
                brojac_za_linkove += listaLinkova[reci._element]
                
        vrednost_ranga = (brojac_za_graf + brojac_za_linkove + brojac_za_reci)
        recnik_ranga = {}
        recnik_ranga[link] = vrednost_ranga/10
        lista_Rangiranja.append(recnik_ranga)
            
if __name__ == '__main__':
    #pickle.dump([t, g], open("imeFajla.obj","wb"))
    lista = []
    g = Graph()
    t = Trie()
    t, g = pickle.load(open("imeFajla.obj","rb"))
    if os.path.lexists("C:\Python27\python-2.7.7-docs-html"):
        pronadji_ucitaj_fajlove("C:\Python27\python-2.7.7-docs-html",lista)
    flag = True
    while flag:
        r = raw_input("Unesite tekst za pretragu: ")
        if not t.has_word(r):
            print "Nepostojeca rec!!!"
            pass
        else:
            lista_Rangiranja = []
            if t.has_word(r):
                listaLinkova = t.getLink(r)
                rangiranje(listaLinkova)
            listaSort = []   
            bablesort(lista_Rangiranja)
            #print lista_Rangiranja
            for i in lista_Rangiranja:
                kljuc = i.keys()[0]
                print kljuc," ",i[kljuc]
        
        odluka = raw_input("Izlaz(da/Enter da ponovite): ").lower()
        if odluka == "da":
            flag = False
        else:
            flag = True
    