from moto import Moto
import veicolo
import auto


alfabeto = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
numeri = ["1","2","3","4","5","6","7","8","9","0"]

def targaValida(targa) -> bool:
    
    if targa[0] not in alfabeto or targa[1] not in alfabeto or targa[2] not in numeri or targa[3] not in numeri or targa[4] not in numeri or targa[5] not in alfabeto or targa[6] not in alfabeto:
        return False
    return True

class PostoMezzo:
    
    def __init__(self, occupato: bool = None, tipologia: str = None, targa: str = None, oreSosta: int = None):
    
        if occupato == None:
            raise ValueError("Specificare se il posto è libero o occupato")
        self.__occupato = occupato
        
        if tipologia == None:
            raise ValueError("Specificare la tipologia di posto")
        self.__tipologia = tipologia
        
        if not occupato and (targa != None or oreSosta != None):
            raise ValueError("Un posto libero non può avere targa o oreSosta")
        
        if occupato and (targa == None or oreSosta == None):
            raise ValueError("Un posto occupato deve avere targa e oreSosta")
        
        elif occupato and targa != None and oreSosta != None:
            if len(targa) != 7 or not targaValida(targa):
                raise ValueError("La targa inserita non è valida")
            self.__targa = targa
        
            self.__oreSosta = oreSosta
        
            
            return
              
        self.__targa = targa
        
        self.__oreSosta = oreSosta
        
    def __str__(self):
        return __class__.__name__ + str(self.__dict__)
    
    def __repr__(self):
        return __class__.__name__ + str(self.__dict__)
    
    @property
    def occupato(self):
        return self.__occupato
    
    @occupato.setter
    def occupato(self, value):
        self.__occupato = value
        return
    
    @property
    def tipologia(self):
        return self.__tipologia
    
    @tipologia.setter
    def tipologia(self, value):
        self.__tipologia = value
        return
    
    @property
    def targa(self):
        """ proprietà sola lettura: la targa NON deve essere modificabile """
        return self.__targa
    
    @targa.setter
    def targa(self, value):
        self.__targa = value
    
    @property
    def oreSosta(self):
        return self.__oreSosta
    
    @oreSosta.setter
    def oreSosta(self, value):
        self.__oreSosta = value
        return
    
    def parcheggia(self, V, oreSosta) -> bool:
        if self.occupato:
            return False
        if isinstance(V, Moto) and self.tipologia == "Moto":
            self.occupato = True
            self.targa = V.targa
            self.oreSosta = oreSosta
        
        elif isinstance(V, auto.Auto) and self.tipologia == "Auto":
            self.occupato = True
            self.targa = V.targa
            self.oreSosta = oreSosta
            
        else:
            return False
        
        return True
    
    def libera(self) -> bool:
        if self.occupato:
            self.targa = None
            self.oreSosta = None
            self.occupato = False    
            return True
        
        else:
            return False
#------------------------------------          
                      
# if __name__ == "__main__":
#     
#     moto = Moto("AB123CD", 2, 1)
#     posto = PostoMezzo(False, "Moto", None, None)
#     print(posto)
#     print(posto.parcheggia(moto, 3))
#     print(posto)
#     posto.libera()
#     print(posto)