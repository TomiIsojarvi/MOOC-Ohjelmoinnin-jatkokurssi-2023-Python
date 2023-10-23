# Tee ratkaisusi tähän:
class Sekuntikello:
    def __init__(self):
        self.sekunnit = 0
        self.minuutit = 0

    def tick(self):
        if self.sekunnit == 59:
            self.sekunnit = 0
            if self.minuutit == 59:
                self.minuutit = 0
            else:
                self.minuutit += 1
        else:
            self.sekunnit += 1

    def __str__(self):
        return f"{self.minuutit:02}:{self.sekunnit:02}"

if __name__ == "__main__":
    kello = Sekuntikello()
    for i in range(3600):
        print(kello)
        kello.tick()