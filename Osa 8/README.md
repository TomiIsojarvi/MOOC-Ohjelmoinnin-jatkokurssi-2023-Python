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
Listan alkioiden arvot ovat viittauksia olioihin. Tämä pätee myös silloin, kun mallinnetaan matriisia: jokainen päälistan alkion arvo on viittaus toiseen listaan (jonka alkiot taas ovat viittauksia arvoihin).

Tee funktio rivien_summat(matriisi: list), joka saa parametrikseen kokonaislukuja sisältävän matriisin.

Funktio lisää jokaiselle matriisin riville uuden alkion, jonka arvo on rivin alkioiden summa. Funktio ei palauta mitään, vaan muokkaa parametrinaan saamaansa matriisia.

Esimerkki funktion kutsumisesta:
```
matriisi = [[1, 2], [3, 4]]
rivien_summat(matriisi)
print(matriisi)
```
```
[[1, 2, 3], [3, 4, 7]]
```
## Vuodet listaan
Tee funktio vuodet_listaan(paivamaarat: list), joka saa parametrikseen listan, joka sisältää date-tyyppisiä olioita. Funktio palauttaa uuden listan, jossa on päivämäärien vuodet suuruusjärjestyksessä pienimmästä suurimpaan.

Esimerkki funktion kutsumisesta:
```
paiva1 = date(2019, 2, 3)
paiva2 = date(2006, 10, 10)
paiva3 = date(1993, 5, 9)

vuodet = vuodet_listaan([paiva1, paiva2, paiva3])
print(vuodet)
```
```
[1993, 2006, 2019]
```
## Kauppalista
Tehtäväpohjassa on määritelty valmiiksi Kauppalista-luokka, jolla voidaan mallintaa yhtä kauppalistaa.

Jos kauppalistaolio on tallennettu esimerkiksi muuttujaan kauppalista, sitä voidaan käsitellä seuraavan esimerkin mukaisesti:
```
print(kauppalista.tuotteita())
print(kauppalista.tuote(1))
print(kauppalista.maara(1))
print(kauppalista.tuote(2))
print(kauppalista.maara(2))
```
```
2
Banaanit
4
Maito
1
```
Myös seuraava onnistuu:
```
# kauppalistalla tuotteet on indeksöity ykkösestä alkaen
for i in range(1, kauppalista.tuotteita()+1):
    tuote = kauppalista.tuote(i)
    maara = kauppalista.maara(i)
    print(f"{tuote}: {maara} kpl")
```
```
banaanit 4 kpl
maito 1 kpl
```
Kauppalistat siis käyttäytyvät hieman listojen tavoin, mutta niitä käsitellään kuitenkin kauppalistan tarjoamien metodien kautta. Toisin kuin listoissa, kauppalistan tuotteet on numeroitu ykkösestä alkaen.

Tee esimerkkejä hyödyntäen funktio tuotteita_yhteensa(lista: Kauppalista), joka saa parametrikseen Kauppalista-tyyppisen olion. Funktio laskee listalla yhteensä olevien tuotteiden määrän ja palauttaa sen.

Huomaa, että kauppalistalla tuotteet indeksoidaan ykkösestä alkaen, ei nollasta. Voit testata ohjelmaasi esim. tällä esimerkkikoodilla:
```
if __name__ == "__main__":
    lista = Kauppalista()
    lista.lisaa("banaanit", 10)
    lista.lisaa("omenat", 5)
    lista.lisaa("ananas", 1)

    print(tuotteita_yhteensa(lista))
```
```
16
```
## Kirja
Tee luokka Kirja, jolla on attribuutteina muuttujat nimi, kirjoittaja, genre ja kirjoitusvuosi sekä konstruktori, joka alustaa muuttujat.

Luokkaa käytetään seuraavasti:
```
python = Kirja("Fluent Python", "Luciano Ramalho", "ohjelmointi", 2015)
everest = Kirja("Huipulta huipulle", "Carina Räihä", "elämänkerta", 2010)

print(f"{python.kirjoittaja}: {python.nimi} ({python.kirjoitusvuosi})")
print(f"Kirjan {everest.nimi} genre on {everest.genre}")
```
```
Luciano Ramalho: Fluent Python (2015)
Kirjan Huipulta huipulle genre on elämänkerta
```
## Kirjoita luokat
Kirjoita alla pyydetyt luokat. Jokaisen luokan alle on kuvattu attribuuttien nimet ja tyypit.

Kirjoita jokaiselle luokalle myös konstruktori, jossa attribuutit annetaan siinä järjestyksessä kuin ne on kuvauksessa annettu.

1. Luokka Muistilista
- attribuutti otsikko (merkkijono)
- attribuutti merkinnat (lista)
2. Luokka Asiakas
- attribuutti tunniste (merkkijono)
- attribuutti saldo (desimaaliluku)
- attribuutti alennusprosentti (kokonaisluku)
3. Luokka Kaapeli
- attribuutti malli (merkkijono)
- attribuutti pituus (desimaaliluku)
- attribuutti maksiminopeus (kokonaisluku)
- attribuutti kaksisuuntainen (totuusarvo)
## Muodosta lemmikki
Määrittele luokka Lemmikki. Luokalla on konstruktori, jossa annetaan arvot attribuuteille nimi, laji ja syntymavuosi tässä järjestyksessä.

Kirjoita sitten luokan ulkopuolelle funktio uusi_lemmikki(nimi: str, laji: str, syntymavuosi: int), joka luo ja palauttaa uuden Lemmikki-tyyppisen (eli Lemmikki-luokkaa vastaavan) olion.

Esimerkki funktion kutsumisesta:
```
musti = uusi_lemmikki("Musti", "koira", 2017)
print(musti.nimi)
print(musti.laji)
print(musti.syntymavuosi)
```
```
Musti
koira
2017
```
## Vanhempi kirja
Tee funktio vanhempi_kirja(kirja1: Kirja, kirja2: Kirja), joka saa parametriksi kaksi Kirja-oliota. Funktio kertoo, kumpi kirjoista on vanhempi.

Funktiota käytetään seuraavasti:
```
python = Kirja("Fluent Python", "Luciano Ramalho", "ohjelmointi", 2015)
everest = Kirja("Huipulta huipulle", "Carina Räihä", "elämänkerta", 2010)
norma = Kirja("Norma", "Sofi Oksanen", "rikos", 2015)

vanhempi_kirja(python, everest)
vanhempi_kirja(python, norma)
```
```
Huipulta huipulle on vanhempi, se kirjoitettiin 2010
Fluent Python ja Norma kirjoitettiin 2015
```
## Genren kirjat
Tee funktio genren_kirjat(kirjat: list, genre: str), joka saa parametriksi listan Kirja-olioita sekä genren kertovan merkkijonon.

Funktio palauttaa uuden listan, jolle se laittaa parametrina olevista kirjoista ne, joilla on haluttu genre.

Funktiota käytetään seuraavasti:
```
python = Kirja("Fluent Python", "Luciano Ramalho", "ohjelmointi", 2015)
everest = Kirja("Huipulta huipulle", "Carina Räihä", "elämänkerta", 2010)
norma = Kirja("Norma", "Sofi Oksanen", "rikos", 2015)

kirjat = [python, everest, norma, Kirja("Lumiukko", "Jo Nesbø", "rikos", 2007)]

print("rikoskirjoja ovat")
for kirja in genren_kirjat(kirjat, "rikos"):
    print(f"{kirja.kirjoittaja}: {kirja.nimi}")
```
```
rikoskirjoja ovat
Sofi Oksanen: Norma
Jo Nesbø: Lumiukko
```
## Vähenevä laskuri
## Etu- ja sukunimi
## Lukutilasto
## Sekuntikello
## Kello
## Maksukortti
## Sarja
