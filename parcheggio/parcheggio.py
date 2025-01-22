from moto import Moto
from auto import Auto
from postoMezzo import PostoMezzo

class Parcheggio:
    def __init__(self, postiAuto = None, postiMoto = None):
        
        if postiAuto == None and postiMoto == None:
            self.__postiAuto = [PostoMezzo(False, "Auto") for x in range(1000)]
            self.__postiMoto = [PostoMezzo(False, "Moto") for x in range(200)]   
    
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

#----------------------------------------------

# if __name__ == "__main__":
#     moto1 = Moto("AB123CD", 2, 1)
#     moto2 = Moto("AF425ER", 1, 1)
#     auto1 = Auto("JK198QC", 5, 3, 200, 500)
#     auto2 = Auto("QE826BC", 5, 1, 200, 500)
#     parcheggio = Parcheggio()
#     pagamento = parcheggio.pagaParcheggio(moto1, 3)
#     print(pagamento)
#     print(parcheggio.pagaParcheggio(auto1, 3))
#     print(parcheggio.totaleGuadagno())
#     print(parcheggio.postiLiberi("Auto"))
#     print(parcheggio.postiLiberi("Moto"))