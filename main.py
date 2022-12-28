from genestski import *
import matplotlib as mpl
from matplotlib import pyplot as plt

def main():
    #generisemo pocetnu populaciju i definisemo promenljive
    populacija = generisi_pocetne_hromozome(10)
    najbolji_rasporedi = []
    najbolje_vrednosti = []
    #petlja koja iterira max broj iteracija
    for i in range(100):
        rangirani_roditelji = rangiraj(populacija)
        najbolje_vrednosti.append(izracunaj_fitnes(rangirani_roditelji[0]))
        najbolji_rasporedi.append(rangirani_roditelji[0])
        parovi = rulet_selekcija(rangirani_roditelji)
        # print(parovi)
        # print()
        deca = ukrstanje(parovi)
        # print(deca)
        # print()
        deca = mutiraj(deca, 0.1)
        # print(deca)
     
        rangirana_deca = rangiraj(deca)
        # print(rangirana_deca)
        # print()
        #rangiramo i napravimo parove
        #ukrstanje
        #mutacija dece
        #elitizam cime se dobija nova populacija
        populacija = elitizam(rangirani_roditelji, rangirana_deca, 0.5)
        print(populacija)
    #iscrtamo
    x = [i for i in range(len(najbolje_vrednosti))]
    plt.plot(x, najbolje_vrednosti)
    plt.show()

if __name__ == "__main__":
    main()