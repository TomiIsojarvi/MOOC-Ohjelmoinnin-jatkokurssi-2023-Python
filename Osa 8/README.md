# Osa 8 - Tehtävien vastaukset
## Pienin keskiarvo
Tee funktio pienin_keskiarvo(henkilo1: dict, henkilo2: dict, henkilo3: dict), joka saa parametrikseen kolme sanakirjaoliota.

Jokaisessa sanakirjaoliossa on alkiot, joihin viittaavat nämä avaimet:

"nimi": kilpailijan nimi
"tulos1": kilpailijan ensimmäinen tulos (kokonaisluku väliltä 1...10)
"tulos2": kilpailijan toinen tulos (kuten yllä)
"tulos3": kilpailijan kolmas tulos (kuten yllä)
Funktio laskee kaikkien kilpailijoiden tulosten keskiarvot ja palauttaa sen kilpailijan, jonka keskiarvo on pienin. Funktion palautusarvona on sanakirjaolio.

Voit olettaa, että vain yhdellä henkilöllä on pienin keskiarvo.

Esimerkki funktion kutsumisesta:
```
henkilo1 = {"nimi": "Keijo", "tulos1": 2, "tulos2": 3, "tulos3": 3}
henkilo2 = {"nimi": "Reijo", "tulos1": 5, "tulos2": 1, "tulos3": 8}
henkilo3 = {"nimi": "Veijo", "tulos1": 3, "tulos2": 1, "tulos3": 1}

print(pienin_keskiarvo(henkilo1, henkilo2, henkilo3))
```
```
{'nimi': 'Veijo', 'tulos1': 3, 'tulos2': 1, 'tulos3': 1}
```
## Rivien summat
## Vuodet listaan
## Kauppalista
## Kirja
## Kirjoita luokat
## Muodosta lemmikki
## Vanhempi kirja
## Genren kirjat
## Vähenevä laskuri
## Etu- ja sukunimi
## Lukutilasto
## Sekuntikello
## Kello
## Maksukortti
## Sarja
