# Edoardo Pretini 4BS
alimOk = ("benzina", "diesel", "elettrico", "metano", "GPL")
marchiOk = ("fiat", "toyota", "audi", "bmw", "mercedes", "subaru", "beta")
modelliOk = ("panda", "yaris", "a3", "serie3", "classeA", "impreza", "enduro")
coloriOk = ("rosso", "grigio", "nero", "bianco", "blu")
alfabeto = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
numeri = ["1","2","3","4","5","6","7","8","9","0"]


def targaValida(targa) -> bool:
    
    if targa != "":
        if targa[0] not in alfabeto or targa[1] not in alfabeto or targa[2] not in numeri or targa[3] not in numeri or targa[4] not in numeri or targa[5] not in alfabeto or targa[6] not in alfabeto:
            return False
    return True



class Veicolo:
    def __init__(self, targa = None, marca = None, modello = None, colore = None, cilindrata = None, alimentazione = None):
        
        if not targa:
            raise ValueError("La targa inserita non è valida")
        
        if len(targa) != 7 or not targaValida(targa):
            raise ValueError("La targa inserita non è valida")
        self.__targa = targa
            
        if marca and marca not in marchiOk:
            raise ValueError("La marca inserita non è valida")
        self.__marca = marca
        
        if modello and modello not in modelliOk:
            raise ValueError("Il modello inserito non è valido")        
        self.__modello = modello
        
        if colore and colore not in coloriOk:
            raise ValueError("Il colore inserito non è valido")
        self.__colore = colore
        
        if cilindrata and (cilindrata <= 0 or cilindrata % 100 != 0):
            raise ValueError ("La cilindrata inserita non è valida")
        self.__cilindrata = cilindrata
        
        if alimentazione and alimentazione not in alimOk:
            raise ValueError("L'alimentazione inserita non è valida")
        self.__alimentazione = alimentazione
            
        return
            
        
    def __str__(self):
        return __class__.__name__ + str(self.__dict__)
    
    def __repr__(self):
        return __class__.__name__ + str(self.__dict__)

    @property
    def targa(self):
        """ proprietà sola lettura: la targa NON deve essere modificabile """
        return self.__targa
    
    @property
    def marca(self):
        return self.__marca
        
    @marca.setter
    def marca(self, value):
        if value not in marchiOk:
            raise ValueError("marca non accettabile")
            self.__marca = value
            return
    
    @property
    def modello(self):
        return self.__modello
    
    @modello.setter
    def modello(self, value):
        if value not in modelliOk:
            raise ValueError("modello non accettabile")
            self.__modello = value
            return
    
    @property
    def colore(self):
        return self.__colore
    
    @colore.setter
    def colore(self, value):
        if value not in coloriOk:
            raise ValueError("colore non accettabile")
            self.__colore = value
            return

    @property
    def cilindrata(self):
        return self.__cilindrata

    @cilindrata.setter
    def cilindrata(self,value):
        if value > 0 and value % 100 == 0:
            self.__cilindrata = value
            return
            raise ValueError("Cilindrata non accettabile")

    @property
    def alimentazione(self):
        return self.__alimentazione
        
    @alimentazione.setter
    def alimentazione(self, value):
        if value not in alimOk:
            raise ValueError("alimentazione non valida")
            self.__alimentazione = value
            return
    
    def __lt__(self, other):
    
        if self.marca < other.marca:
            return True
        
        if self.marca == other.marca and self.modello < other.modello:
            return True
        
        
        if self.marca == other.marca and self.modello == other.modello and self.cilindrata < other.cilindrata: 
            return True
    
        return False

#---------------------------------------------

if __name__ == "__main__":
    
    veicolo1 = Veicolo("AB123DD","subaru","yaris",None,200)
    print(veicolo1)
    
    veicolo2 = Veicolo("AB123FD","subaru","yaris",None,100)
    print(veicolo2)
    
    print(veicolo1 < veicolo2)