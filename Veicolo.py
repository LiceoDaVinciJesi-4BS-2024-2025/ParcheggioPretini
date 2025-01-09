# Edoardo Pretini 4BS

alfabeto = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]

class Veicolo:
    def __init__(self, marca = "", modello = "", colore = "", cilindrata = 0, alimentazione = "", targa = ""):
        
        self.__marca = marca
        self.__modello = modello
        self.__colore = colore
        
        if cilindrata <= 0 or cilindrata % 100 != 0:
            raise ValueError ("La cilindrata inserita non è valida")
        self.__cilindrata = cilindrata
        return
            
        self.__alimentazione = alimentazione
        
     
        def __str__(self):
        return __class__.__name__ + str(self.__dict__)