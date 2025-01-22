import veicolo

class Auto(veicolo.Veicolo):
    
    def __init__(self, targa: str, passeggeriMassimi: int, numeroPasseggeri: int, kgTrasportati: int, kgMassimi: int):
        
        super().__init__(targa)
        if passeggeriMassimi <= 0 or passeggeriMassimi > 5:
            raise ValueError("Il numero di passeggeri massimi non è accettabile")
        self.__passeggeriMassimi = passeggeriMassimi
        
        if numeroPasseggeri > passeggeriMassimi or numeroPasseggeri <= 0:
            raise ValueError("Il numero di passeggeri non è valido o supera il limite consentito")
        self.__numeroPasseggeri = numeroPasseggeri
        #guarda se devi trasportare anche le altre funzioni
        
        if kgMassimi <= 0 or kgMassimi > 500:
            raise ValueError("Il numero di kg massimi non è accettabile")
        self.__kgMassimi = kgMassimi
        
        if kgTrasportati > kgMassimi or kgTrasportati <= 0:
            raise ValueError("Il numero di kg non è valido o supera il limite consentito")
        self.__kgTrasportati = kgTrasportati
        
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
        if numero <= 0 or numero > 5:
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
    
    @property
    def kgMassimi (self):
        return self.__kgMassimi
    
    @passeggeriMassimi.setter
    def kgMassimi(self, numero:int):
        """
        permette di reimpostare il numero massimo di passeggeri
        """
        if numero <= 0 or numero > 500:
            raise ValueError("Valore non accettabile")
        self.__kgMassimi = numero
        return
    
    @property
    def kgTrasportati(self):
        return self.__kgTrasportati
    
    @kgTrasportati.setter
    def kgTrasportati(self, numero:int):
        """
        permette di reimpostare le persone trasportate
        """
        if numero <= 0 or numero > self.__kgMassimi:
            raise ValueError("Valore non accettabile")
        self.__kgTrasportati = numero
        return
    
#-----------------------------------------------------------------------------------------------------
#TEST
# if __name__ == "__main__":
#     #creo un'auto
#     auto1 = Auto("AB123CD", 5, 3, 200, 500)
#     auto1.marca = "subaru"
#     auto1.passeggeriMassimi = 5
#     auto1.numeroPasseggeri = 3
#     auto1.kgTrasportati = 200
#     auto1.kgMassimi = 500
#     print(auto1)