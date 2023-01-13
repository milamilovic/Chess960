from genestski import *
import matplotlib as mpl
from matplotlib import pyplot as plt

def main():
    #generisemo pocetnu populaciju i definisemo promenljive
    populacija = generisi_pocetne_hromozome(10)
    najbolji_rasporedi = []
    najbolje_vrednosti = []
    kopija_populacije = [i for i in populacija]
    rangirani_roditelji = rangiraj(kopija_populacije)
    nacrtaj(rangirani_roditelji, 10)
    najbolje_vrednosti = [izracunaj_fitnes(rangirani_roditelji[i]) for i in range(9, -1, -1)]
    najbolji_rasporedi = [rangirani_roditelji[i] for i in range(9, -1, -1)]
    #petlja koja iterira max broj iteracija
    for i in range(100):
        #rangiramo i napravimo parove
        rangirani_roditelji = rangiraj(populacija)
        najbolje_vrednosti.append(izracunaj_fitnes(rangirani_roditelji[0]))
        najbolji_rasporedi.append(rangirani_roditelji[0])
        parovi = rulet_selekcija(rangirani_roditelji)
        #ukrstanje
        deca = ukrstanje(parovi)
        #mutacija dece
        deca = mutiraj(deca, 0.1)
        rangirana_deca = rangiraj(deca)
        #elitizam cime se dobija nova populacija
        populacija = elitizam(rangirani_roditelji, rangirana_deca, 0.5)
        nacrtaj(populacija, 0)
    #iscrtamo
    x = [i for i in range(len(najbolje_vrednosti))]
    plt.plot(x, najbolje_vrednosti)
    plt.show()

# 1  -  top
# 2  -  konj
# 3  -  lovac
# 4  -  kraljica
# 5  -  kralj
figure = {
1: u'\u2656',
2: u'\u2658',
3: u'\u2657',
4: u'\u2655',
5: u'\u2654'
}

prethodna_najbolja = ""

#funkcija koja iscrtava prvih x pozicija trenutne populacije
def nacrtaj(tabla, x):
    global prethodna_najbolja
    ispis = ""
    if(x!=len(tabla)):
        for figura in tabla[0]:
            ispis += str(figure[figura])
            ispis += "  "
        ispis += "  -->    fitnes vrednost je "
        ispis += str(izracunaj_fitnes(tabla[0]))
        if(ispis != prethodna_najbolja):
            print()
            print(ispis)
        prethodna_najbolja = ispis
        ispis = ""
    else:
        for i in range(x-1, -1, -1):
            for figura in tabla[i]:
                ispis += str(figure[figura])
                ispis += "  "
            ispis += "  -->    fitnes vrednost je "
            ispis += str(izracunaj_fitnes(tabla[i]))
            if(ispis != prethodna_najbolja):
                print()
                print(ispis)
            prethodna_najbolja = ispis
            ispis = ""

if __name__ == "__main__":
    main()