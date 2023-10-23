# Tee ratkaisusi tähän:
class  Lukutilasto:
    def __init__(self):
        self.lukujen_summa = 0
        self.lukuja = 0

    def lisaa_luku(self, luku:int):
        self.lukuja += 1
        self.lukujen_summa += luku

    def lukujen_maara(self):
        return self.lukuja
    
    def summa(self):
        return self.lukujen_summa
    
    def keskiarvo(self):
        if (self.lukuja != 0):
            return self.lukujen_summa / self.lukuja

def main():
    tilasto = Lukutilasto()
    tilasto_parilliset = Lukutilasto()
    tilasto_parittomat = Lukutilasto()

    print("Anna lukuja:")

    while True:
        luku = int(input())

        if luku == -1:
            break

        tilasto.lisaa_luku(luku)

        if (luku % 2 == 0):
            tilasto_parilliset.lisaa_luku(luku)
        else:
            tilasto_parittomat.lisaa_luku(luku)

    print("Summa:", tilasto.summa())
    print("Keskiarvo:", tilasto.keskiarvo())
    print("Parillisten summa:", tilasto_parilliset.summa())
    print("Parittomien summa:", tilasto_parittomat.summa())

main()