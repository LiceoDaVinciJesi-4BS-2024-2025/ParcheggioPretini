from veicolo import Veicolo

class Moto(Veicolo):
    def __init__(self, marca = "", modello = "", colore = "", cilindrata = 0, alimentazione = "", targa = "", passeggeriMassimi: int = 2, numeroPasseggeri: int = 1, chiliMassimi : int = 200, chiliTrasportati : int = 75):
        super().__init__(marca, modello, colore, cilindrata, alimentazione, targa)
        
    if passeggeriMassimi < 1:
        raise ValueError("La targa inserita non è valida")
    self.__targa = targa
        
        
        
        
        
        
    def __str__(self):
            return __class__.__name__ + str(self.__dict__)