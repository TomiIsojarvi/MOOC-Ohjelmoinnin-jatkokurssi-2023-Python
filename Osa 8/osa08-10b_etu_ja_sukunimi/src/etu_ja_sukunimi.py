class Henkilo:
  def __init__(self, nimi:str):
    self.nimi = nimi

  def anna_etunimi(self):
    koko_nimi = self.nimi.split(' ')

    return koko_nimi[0]

  def anna_sukunimi(self):
    koko_nimi = self.nimi.split(' ')

    return koko_nimi[1]
  
if __name__ == "__main__":
  pekka = Henkilo("Pekka Python")
  print(pekka.anna_etunimi())
  print(pekka.anna_sukunimi())

  pauli = Henkilo("Pauli Pythonen")
  print(pauli.anna_etunimi())
  print(pauli.anna_sukunimi())