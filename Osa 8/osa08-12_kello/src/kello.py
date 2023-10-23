# Tee ratkaisusi tähän:
class Kello:
    def __init__(self, tunnit: int, minuutit: int, sekunnit: int):
        self.tunnit = tunnit
        self.minuutit = minuutit
        self.sekunnit = sekunnit

    def tick(self):
        if self.sekunnit == 59:
            self.sekunnit = 0
            if self.minuutit == 59:
                self.minuutit = 0
                if self.tunnit == 23:
                    self.tunnit = 0
                else:
                    self.tunnit += 1
            else:
                self.minuutit += 1
        else:
            self.sekunnit += 1

    def aseta(self, tunnit: int, minuutit: int):
        self.tunnit = tunnit
        self.minuutit = minuutit
        self.sekunnit = 0

    def __str__(self):
        return f"{self.tunnit:02}:{self.minuutit:02}:{self.sekunnit:02}"

if __name__ == "__main__":
    kello = Kello(23, 59, 55)
    print(kello)
    kello.tick()
    print(kello)
    kello.tick()
    print(kello)
    kello.tick()
    print(kello)
    kello.tick()
    print(kello)
    kello.tick()
    print(kello)
    kello.tick()
    print(kello)

    kello.aseta(12, 5)
    print(kello)