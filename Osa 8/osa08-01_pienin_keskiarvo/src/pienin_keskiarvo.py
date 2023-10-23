def pienin_keskiarvo(henkilo1: dict, henkilo2: dict, henkilo3: dict):
  keskiarvo1 = 0
  keskiarvo2 = 0
  keskiarvo3 = 0

  keskiarvo1 = (henkilo1["tulos1"] + henkilo1["tulos2"] + henkilo1["tulos3"]) / 3
  keskiarvo2 = (henkilo2["tulos1"] + henkilo2["tulos2"] + henkilo2["tulos3"]) / 3
  keskiarvo3 = (henkilo3["tulos1"] + henkilo3["tulos2"] + henkilo3["tulos3"]) / 3

  if keskiarvo1 < keskiarvo2 and keskiarvo1 < keskiarvo3:
    return henkilo1
  elif keskiarvo2 < keskiarvo3:
    return henkilo2
  else:
    return henkilo3