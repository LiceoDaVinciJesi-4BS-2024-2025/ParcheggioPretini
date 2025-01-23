import veicolo

class Moto(veicolo.Veicolo):
    
    def __init__(self, targa: str, passeggeriMassimi: int, numeroPasseggeri: int):
        
        super().__init__(targa)
        if passeggeriMassimi <= 0 or passeggeriMassimi > 2:
            raise ValueError("Il numero di passeggeri massimi non è accettabile")
        self.__passeggeriMassimi = passeggeriMassimi
        
        if numeroPasseggeri > passeggeriMassimi or numeroPasseggeri <= 0:
            raise ValueError("Il numero di passeggeri non è valido o supera il limite consentito")
        self.__numeroPasseggeri = numeroPasseggeri
        #guarda se devi trasportare anche le altre funzioni
    
    def __str__(self):
        return __class__.__name__ + str(self.__dict__)
    def __repr__(self):
        return __class__.__name__ + str(self.__dict__)
        
    @property
    def passeggeriMassimi (self):
        return self.__passeggeriMassimi
    
    @passeggeriMassimi.setter
    def passeggeriMassimi(self, numero:int):
        """
        permette di reimpostare il numero massimo di passeggeri
        """
        if numero <= 0 or numero > 2:
            raise ValueError("Valore non accettabile")
        self.__passeggeriMassimi = numero
        return

    @property
    def numeroPasseggeri (self):
        return self.__numeroPasseggeri
    
    @numeroPasseggeri.setter
    def numeroPasseggeri(self, numero:int):
        """
        permette di reimpostare le persone trasportate
        """
        if numero <= 0 or numero > self.__passeggeriMassimi:
            raise ValueError("Valore non accettabile")
        self.__numeroPasseggeri = numero
        return
    
    
#-----------------------------------------------------------------------------------------------------
#TEST
#if __name__ == "__main__":
    #creo una moto
#    moto1 = Moto("AB123CD", 2, 1)
#     moto1.marca = "fiat"
#     moto1.passeggeriMassimi = 1
#     moto1.numeroPasseggeri = 1
#     print(moto1)