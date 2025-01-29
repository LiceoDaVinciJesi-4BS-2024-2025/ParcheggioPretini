from pathlib import Path
from moto import Moto
from auto import Auto
from postoMezzo import PostoMezzo

class Parcheggio:
    def __init__(self, postiAuto = None, postiMoto = None):
        
        if postiAuto == None and postiMoto == None:
            self.__postiAuto = [PostoMezzo(False, "Auto") for x in range(1000)]
            self.__postiMoto = [PostoMezzo(False, "Moto") for x in range(200)]   
    
    def __str__(self):
        a = "Parcheggio: " + str(self.__dict__)
        return a
                
    
    def parcheggiaVeicolo(self, tipologia, veicolo, oreSosta):
        
        if tipologia == "Auto":
            lista = self.__postiAuto
        else:
            lista = self.__postiMoto
        
        for parcheggio in lista:
            if parcheggio.occupato == False:
                parcheggio.parcheggia(veicolo, oreSosta)
                break
    
    def liberaParcheggio(self, tipologia, targa):
        
        if tipologia == "Auto":
            lista = self.__postiAuto
        else:
            lista = self.__postiMoto
        
        for parcheggio in lista:
            if parcheggio.targa == targa:
                parcheggio.libera()
                break
            
    def postiLiberi(self, tipologia) -> int:
        cnt = 0

        if tipologia == "Moto":
            for elem in self.__postiMoto:
                if elem.occupato == False:
                    cnt += 1
                
        elif tipologia == "Auto":
            for elem in self.__postiAuto:
                if elem.occupato == False:
                    cnt += 1
        return cnt
    
    
    def pagaParcheggio(self, veicolo, oreSosta) -> int:
        
        if isinstance(veicolo, Auto):
            for elem in self.__postiAuto:
                if elem.occupato == False:
                    elem.parcheggia(veicolo, oreSosta)
                    totale = oreSosta * 1.5
                    break
        
        elif isinstance(veicolo, Moto):
            for elem in self.__postiMoto:
                if elem.occupato == False:
                    elem.parcheggia(veicolo, oreSosta)
                    totale = oreSosta * 1.2
                    break
        
        return totale
    
    def totaleGuadagno(self) -> int:
        totaleMoto = 0
        totaleAuto = 0
        
        for elem in self.__postiAuto:
            if elem.occupato:
                totaleAuto += (elem.oreSosta * 1.5)
        
        for elem in self.__postiMoto:
            if elem.occupato:
                totaleMoto += (elem.oreSosta * 1.2)

        return (totaleAuto + totaleMoto) / 2

# Perché se tolgo il diviso 2 porta il doppio?

#--------------------------------------------

if __name__ == "__main__":
    
    parcheggio1 = Parcheggio()
    moto = Moto("AB123CD", 2, 1)
    auto = Auto("DG134AT", 5, 3, 200, 500)
    print(moto)
    print(auto)
    parcheggio1.parcheggiaVeicolo("Moto", moto, 2)
    parcheggio1.parcheggiaVeicolo("Auto", auto, 5)
    print(parcheggio1)
    print("Posti moto liberi: " + str(parcheggio1.postiLiberi("Moto")))
    print("Posti auto liberi: " + str(parcheggio1.postiLiberi("Auto")))
    print("Guadagno moto: " + str(parcheggio1.pagaParcheggio(moto, 2)) + "$")
    print("Guadagno auto: " + str(parcheggio1.pagaParcheggio(auto, 5)) + "$")
    print("Totale guadagno: " + str(parcheggio1.totaleGuadagno()) + "$")
    parcheggio1.liberaParcheggio("Auto","DG134AT")
    print(parcheggio1)

# Perché non porta libera parcheggio?
