import numpy as np
import random

def generisi_pocetne_hromozome(broj_jedinki):
    # 1  -  top
    # 2  -  konj
    # 3  -  lovac
    # 4  -  kraljica
    # 5  -  kralj
    osnovna_pozicija = np.array([1, 2, 3, 4, 5, 3, 2, 1])
    jedinke = []
    i = 0
    for i in range(broj_jedinki):
        jedinka = permutuj(osnovna_pozicija)
        jedinke.append(jedinka)
        #print(jedinka)
    return jedinke

def permutuj(osnovna_pozicija):
    pozicija = [0]*len(osnovna_pozicija)
    pozicija_kralja = random.randint(1, 6)
    pozicija[pozicija_kralja] = 5
    pozicija_topa1 = random.randint(0, pozicija_kralja-1)
    pozicija_topa2 = random.randint(pozicija_kralja+1, len(osnovna_pozicija)-1)
    pozicija[pozicija_topa1] = 1
    pozicija[pozicija_topa2] = 1
    while True:
        pozicija_lovca_p = random.randint(0, 7)
        if pozicija_lovca_p%2!=0 or pozicija_lovca_p in [pozicija_kralja, pozicija_topa1, pozicija_topa2]:
            continue
        else:
            break
    pozicija[pozicija_lovca_p] = 3
    while True:
        pozicija_lovca_n = random.randint(0, 7)
        if pozicija_lovca_n%2!=1 or pozicija_lovca_n in [pozicija_kralja, pozicija_topa1, pozicija_topa2]:
            continue
        else:
            break
    pozicija[pozicija_lovca_n] = 3
    while True:
        pozicija_kraljice = random.randint(0, 7)
        if pozicija_kraljice in [pozicija_kralja, pozicija_topa1, pozicija_topa2, pozicija_lovca_n, pozicija_lovca_p]:
            continue
        else:
            break
    pozicija[pozicija_kraljice] = 4
    for i in range(len(pozicija)):
        if pozicija[i]==0:
            pozicija[i] = 2
    return pozicija
    
    

def izracunaj_fitnes(jedinka):
    jedinka = np.array(jedinka)
    osnovna_pozicija = np.array([1, 2, 3, 4, 5, 3, 2, 1])
    vrednost = 0
    pozicije = np.where(jedinka == 3)[0]
    if(len(pozicije)!=2):
        return 1000
    if not((pozicije[0]%2==0 and pozicije[1]%2==1) or (pozicije[1]%2==0 and pozicije[0]%2==1)):
        return 1000
    pozicije_topova = np.where(jedinka == 1)[0]
    pozicija_kralja = np.where(jedinka == 5)[0]
    if(len(pozicija_kralja)!=1 or len(pozicije_topova)!=2):
        return 1000
    if not((pozicija_kralja[0]>pozicije_topova[0] and pozicija_kralja[0]< pozicije_topova[1]) or
    (pozicija_kralja[0]<pozicije_topova[0] and pozicija_kralja[0]> pozicije_topova[1])):
        return 1000
    for i in range(0, 5):
        for j in range(len(jedinka)):
            if osnovna_pozicija[i]==jedinka[j]:
                vrednost += abs(j-i)
                break
    for i in range(5, 8):
        for j in range(len(jedinka)-1, -1, -1):
            if osnovna_pozicija[i]==jedinka[j]:
                vrednost += abs(j-i)
                break
    return vrednost

def rangiraj(populacija):
    rangirana_populacija = []
    fitnes_vrednosti = []
    for roditelj in populacija:
        fitnes = izracunaj_fitnes(roditelj)
        fitnes_vrednosti.append(fitnes)
    duzina = len(populacija)
    for i in range(duzina):
        indeks = np.argmin(fitnes_vrednosti)
        rangirana_populacija.append(populacija[indeks])
        del populacija[indeks]
        del fitnes_vrednosti[indeks]
    return rangirana_populacija
    
#rulet selekcija iz materijala sa vezbi
#bazirano na polu nasumicnoj dodeli
def rulet_selekcija(parents):
  pairs = []
  i = 0
  for i in range(0, len(parents), 2):
    weights=[]
    for i in range(len(parents)):
        weights.append((len(parents)-i)*random.random()) #za minimum
      #  weights.append((i+1)*random.random()) #za maksimum
    if (weights[0]>=weights[1]):
        maxInd1=0
        maxInd2=1
    else:
        maxInd1=1
        maxInd2=0
    for i in range(2,len(parents)):
        if weights[i]>weights[maxInd1]:
            maxInd2=maxInd1
            maxInd1=i
        elif weights[i]>weights[maxInd2]:
            maxInd2=1
    pairs.append([parents[maxInd1], parents[maxInd2]])
  return pairs

def ukrstanje(parovi):
    deca = []
    for a, b in parovi:
        a = np.array(a)
        b = np.array(b)
        dete = [0]*len(a)
        pozicija_kralja1 = np.where(a == 5)[0]
        pozicija_kralja2 = np.where(b == 5)[0]
        pozicije_topova1 = np.where(a == 1)[0]
        pozicije_topova2 = np.where(b == 1)[0]
        if (pozicija_kralja1[0]>pozicije_topova2[0] and pozicija_kralja1[0]< pozicije_topova2[1]):
            dete[pozicija_kralja1[0]] = 5
            dete[pozicije_topova2[0]] = 1
            dete[pozicije_topova2[1]] = 1
        elif (pozicija_kralja2[0]>pozicije_topova1[0] and pozicija_kralja2[0]< pozicije_topova1[1]):
            dete[pozicija_kralja2[0]] = 5
            dete[pozicije_topova1[0]] = 1
            dete[pozicije_topova1[1]] = 1
        else:
            dete[pozicija_kralja1[0]] = 5
            dete[pozicije_topova1[0]] = 1
            dete[pozicije_topova1[1]] = 1
        pozicije_lovaca1 = np.where(a == 3)[0]
        pozicije_lovaca2 = np.where(b == 3)[0]
        parni_lovci = []
        neparni_lovci = []
        if pozicije_lovaca1[0]%2==0:
            parni_lovci.append(pozicije_lovaca1[0])
            neparni_lovci.append(pozicije_lovaca1[1])
        else:
            neparni_lovci.append(pozicije_lovaca1[0])
            parni_lovci.append(pozicije_lovaca1[1])
        if pozicije_lovaca2[0]%2==0:
            parni_lovci.append(pozicije_lovaca2[0])
            neparni_lovci.append(pozicije_lovaca2[1])
        else:
            neparni_lovci.append(pozicije_lovaca2[0])
            parni_lovci.append(pozicije_lovaca2[1])
        if dete[parni_lovci[0]]==0 and dete[neparni_lovci[1]]==0:
            dete[parni_lovci[0]] = 3
            dete[neparni_lovci[1]] = 3
        elif dete[parni_lovci[1]]==0 and dete[neparni_lovci[0]]==0:
            dete[parni_lovci[1]] = 3
            dete[neparni_lovci[0]] = 3
        elif dete[parni_lovci[1]]==0 and dete[neparni_lovci[1]]==0:
            dete[parni_lovci[1]] = 3
            dete[neparni_lovci[1]] = 3
        elif dete[parni_lovci[0]]==0 and dete[neparni_lovci[0]]==0:
            dete[parni_lovci[0]] = 3
            dete[neparni_lovci[0]] = 3
        else:
            slobodne = np.where(np.array(dete)==0)[0]
            parne_slobodne = [i for i in slobodne if i%2==0]
            neparne_slobodne = [i for i in slobodne if i%2==1]
            dete[parne_slobodne[random.randint(0, len(parne_slobodne)-1)]] = 3
            dete[neparne_slobodne[random.randint(0, len(neparne_slobodne)-1)]] = 3
        pozicija_kraljice1 = np.where(a==4)[0]
        pozicija_kraljice2 = np.where(b==4)[0]
        if dete[pozicija_kraljice2[0]] == 0:
            dete[pozicija_kraljice2[0]] = 4
        elif dete[pozicija_kraljice1[0]] == 0:
            dete[pozicija_kraljice1[0]] = 4
        else:
            slobodne = np.where(np.array(dete)==0)[0]
            dete[slobodne[random.randint(0, len(slobodne)-1)]] = 4
        for i in range(len(dete)):
            if dete[i]==0:
                dete[i] = 2
        deca.append(dete)
    return deca

def mutiraj(deca, koeficijent_mutacije):
    mutirani = []
    for dete in deca:
        for i in range(len(deca)):
            if random.random()<koeficijent_mutacije:
                r1 = random.randint(0, 7)
                r2 = random.randint(0, 7)
                temp = dete[r1]
                dete[r1] = dete[r2]
                dete[r2] = temp
        mutirani.append(dete)
    return mutirani

def elitizam(roditelji, deca, koeficijent):
    populacija = []
    broj_roditelja = int(np.round(len(roditelji)*koeficijent))
    for i in range(broj_roditelja):
        populacija.append(roditelji[i])
    for i in range(0, len(roditelji)-broj_roditelja):
        populacija.append(deca[i])
    return populacija