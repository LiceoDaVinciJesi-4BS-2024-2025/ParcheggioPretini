from parcheggio import Parcheggio
from auto import Auto
from moto import Moto

if __name__ == "__main__":
    moto1 = Moto("AB123CD", 2, 1)
    moto2 = Moto("AF425ER", 1, 1)
    auto1 = Auto("JK198QC", 5, 3, 200, 500)
    auto2 = Auto("QE826BC", 5, 1, 200, 500)
    parcheggio = Parcheggio()
    pagamento = parcheggio.pagaParcheggio(moto1, 3)
    file = open("park.data", "w")
    file.write("Saldo moto: " + str(pagamento) + " $" + "\n")
    file.write("Saldo auto: " + str(parcheggio.pagaParcheggio(auto1, 3)) + " $" + "\n")
    file.write("Guadagno totale del titolare: " + str(parcheggio.totaleGuadagno()) + " $" + "\n")
    file.write("Numero posti auto occupati: " + str(1000 - parcheggio.postiLiberi("Auto")) + "\n")
    file.write("Numero posti moto occupati: " + str(200 - parcheggio.postiLiberi("Moto")) + "\n")
    file.write("Numero posti auto liberi: " + str(parcheggio.postiLiberi("Auto")) + "\n")
    file.write("Numero posti moto liberi: " + str(parcheggio.postiLiberi("Moto")))
    file.close()

