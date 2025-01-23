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
        totale = 0
        for elem in self.__postiAuto:
            if elem.occupato:
                totale = totale + (elem.oreSosta * 1.5)
        
        for elem in self.__postiMoto:
            if elem.occupato:
                totale = totale + (elem.oreSosta * 1.2)

        return totale
