from pathlib import Path
from moto import Moto
from auto import Auto
from postoMezzo import PostoMezzo

class Parcheggio:
    
    def __init__(self, parcheggioNome: str):
        
        self.__postiAuto = []
        self.__postiMoto = []
        
        for x in range(1000):
            self.__postiAuto.append(PostoMezzo(False, "Auto"))
        
        for x in range(200):
            self.__postiMoto.append(PostoMezzo(False, "Moto"))
 
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
                return True
    
            return False
    
    def liberaPagaParcheggio(self, veicolo, oreSosta):
        
        if isinstance(veicolo, Auto):
            lista = self.__postiAuto
        else:
            lista = self.__postiMoto
        
        for parcheggio in lista:
            if parcheggio.targa == veicolo.targa:
                parcheggio.libera()
                break
        
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
               
    def totaleGuadagno(self) -> int:
        totaleMoto = 0
        totaleAuto = 0
        
        for elem in self.__postiAuto:
            if elem.occupato:
                totaleAuto += (elem.oreSosta * 1.5)
        
        for elem in self.__postiMoto:
            if elem.occupato:
                totaleMoto += (elem.oreSosta * 1.2)

        return (totaleAuto + totaleMoto)
#--------------------------------------------

if __name__ == "__main__":
    
    parcheggio1 = Parcheggio("Marracash Piadina")
    moto = Moto("AB123CD", 2, 1)
    auto = Auto("DG134AT", 5, 3, 200, 500)
    print(moto)
    print(auto)
    parcheggio1.parcheggiaVeicolo("Moto", moto, 2)
    parcheggio1.parcheggiaVeicolo("Auto", auto, 5)
    print(parcheggio1)
    print("Posti moto liberi: " + str(parcheggio1.postiLiberi("Moto")))
    print("Posti auto liberi: " + str(parcheggio1.postiLiberi("Auto")))
    print("Guadagno moto: " + str(parcheggio1.liberaPagaParcheggio(moto, 2)) + "$")
    print("Guadagno auto: " + str(parcheggio1.liberaPagaParcheggio(auto, 5)) + "$")
    print("Totale guadagno: " + str(parcheggio1.totaleGuadagno()) + "$")
    print(parcheggio1)
