# Tee ratkaisusi tähän:
class Sarja:
  def __init__(self, nimi:str, kaudet: int, genret: list):
    self.nimi = nimi
    self.kaudet = kaudet
    self.genret = genret
    self.arvosanat = []

  def __str__(self):
    nimi = self.nimi
    kaudet = self.kaudet
    genret = ", ".join(self.genret)
    maara = len(self.arvosanat)
    arvosana_str = "ei arvosteluja"
    
    if maara > 0:
      summa = sum(self.arvosanat)
      keskiarvo = summa / maara
      arvosana_str = f"arvosteluja {maara}, keskiarvo {keskiarvo: .1f} pistettä"

    else:
      summa = 0
      keskiarvo = 0


    return f"{nimi} ({kaudet} esityskautta)\ngenret: {genret}\n{arvosana_str}"
  def keskiarvo(self):
    return sum(self.arvosanat) / len(self.arvosanat)
  
  def arvostele(self, arvosana):
    if arvosana >= 0  and arvosana <= 5:
      self.arvosanat.append(arvosana)
  

def arvosana_vahintaan(arvosana: float, sarjat: list):
  palautus_lista = []

  for sarja in sarjat:
    if sum(sarja.arvosanat) / len(sarja.arvosanat) >= arvosana:
      palautus_lista.append(sarja)

  return palautus_lista
  
def sisaltaa_genren(genre: str, sarjat: list):
  palautus_lista = []

  for sarja in sarjat:
    if genre in sarja.genret:
      palautus_lista.append(sarja)

  return palautus_lista

# s1 = Sarja("Dexter", 8, ["Crime", "Drama", "Mystery", "Thriller"])
# s1.arvostele(5)

# s2 = Sarja("South Park", 24, ["Animation", "Comedy"])
# s2.arvostele(3)

# s3 = Sarja("Friends", 10, ["Romance", "Comedy"])
# s3.arvostele(2)

# sarjat = [s1, s2, s3]

# print("arvosana vähintään 4.5:")
# for sarja in arvosana_vahintaan(4.5, sarjat):
#   print(sarja.nimi)

# print("genre Comedy:")
# for sarja in sisaltaa_genren("Comedy", sarjat):
#     print(sarja.nimi)

