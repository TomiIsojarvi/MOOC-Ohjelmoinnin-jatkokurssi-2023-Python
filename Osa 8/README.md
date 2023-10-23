# Osa 8 - Tehtävien vastaukset
## Pienin keskiarvo
Tee funktio pienin_keskiarvo(henkilo1: dict, henkilo2: dict, henkilo3: dict), joka saa parametrikseen kolme sanakirjaoliota.

Jokaisessa sanakirjaoliossa on alkiot, joihin viittaavat nämä avaimet:

- "nimi": kilpailijan nimi
- "tulos1": kilpailijan ensimmäinen tulos (kokonaisluku väliltä 1...10)
- "tulos2": kilpailijan toinen tulos (kuten yllä)
- "tulos3": kilpailijan kolmas tulos (kuten yllä)
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

[Vastaus](osa08-01_pienin_keskiarvo/src/pienin_keskiarvo.py)
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

[Vastaus](osa01-01_hymio/src)
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

[Vastaus](osa01-01_hymio/src)
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

[Vastaus](osa01-01_hymio/src)
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

[Vastaus](osa01-01_hymio/src)
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

[Vastaus](osa01-01_hymio/src)
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

[Vastaus](osa01-01_hymio/src)
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

[Vastaus](osa01-01_hymio/src)
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

[Vastaus](osa01-01_hymio/src)
## Vähenevä laskuri
Tässä tehtävässä on useampi osa. Jokainen osa vastaa yhtä tehtäväpistettä.

Tehtäväpohjan mukana tulee osittain valmiiksi toteutettu luokka VahenevaLaskuri:
```
class VahenevaLaskuri:
    def __init__(self, arvo_alussa: int):
        self.arvo = arvo_alussa

    def tulosta_arvo(self):
        print("arvo:", self.arvo)

    def vahenna(self):
        pass

    # ja tänne muut metodit
```
Luokkaa käytetään seuraavasti
```
laskuri = VahenevaLaskuri(10)
laskuri.tulosta_arvo()
laskuri.vahenna()
laskuri.tulosta_arvo()
laskuri.vahenna()
laskuri.tulosta_arvo()
```
```
arvo: 10
arvo: 9
arvo: 8
```
### Osa 1: Laskurin vähentäminen
Täydennä luokan runkoon metodin vahenna toteutus sellaiseksi, että se vähentää kutsuttavan olion oliomuuttujan arvoa yhdellä. Kun olet toteuttanut metodin vahenna, äskeisen pääohjelman tulee toimia esimerkkitulosteen mukaan.
### Osa 2: Laskurin arvo ei saa olla negatiivinen
Täydennä metodin vahenna toteutus sellaiseksi, ettei laskurin arvo mene koskaan negatiiviseksi: jos laskurin arvo on jo 0, sitä ei enää vähennetä.
```
laskuri = VahenevaLaskuri(2)
laskuri.tulosta_arvo()
laskuri.vahenna()
laskuri.tulosta_arvo()
laskuri.vahenna()
laskuri.tulosta_arvo()
laskuri.vahenna()
laskuri.tulosta_arvo()
```
```
arvo: 2
arvo: 1
arvo: 0
arvo: 0
```
### Osa 3: Laskurin arvon nollaus
Tee laskurille metodi nollaa, joka nollaa laskurin arvon:
```
laskuri = VahenevaLaskuri(100)
laskuri.tulosta_arvo()
laskuri.nollaa()
laskuri.tulosta_arvo()
```
```
arvo: 100
arvo: 0
```
### Osa 4: Alkuperäisen arvon palautus
Tee laskurille metodi palauta_alkuperainen_arvo() joka palauttaa laskurille sen alkuperäisen arvon:
```
laskuri = VahenevaLaskuri(55)
laskuri.vahenna()
laskuri.vahenna()
laskuri.vahenna()
laskuri.vahenna()
laskuri.tulosta_arvo()
laskuri.palauta_alkuperainen_arvo()
laskuri.tulosta_arvo()
```
```
arvo: 51
arvo: 55
```

[Vastaus](osa01-01_hymio/src)
## Etu- ja sukunimi
Kirjoita luokka Henkilo, jolla on ainoastaan yksi attribuutti nimi, joka asetetaan konstruktorissa.

Lisäksi luokalle tule kirjoitaa kaksi metodia:

Metodi anna_etunimi palauttaa henkilön etunimen ja metodi anna_sukunimi vastaavasti henkilön sukunimen.

Voit olettaa metodeissa, että konstruktroissa annetussa nimessä on etu- ja sukunimi välilyönnillä erotettuna eikä muita nimiä.

Esimerkki luokan käytöstä:
```
if __name__ == "__main__":
    pekka = Henkilo("Pekka Python")
    print(pekka.anna_etunimi())
    print(pekka.anna_sukunimi())

    pauli = Henkilo("Pauli Pythonen")
    print(pauli.anna_etunimi())
    print(pauli.anna_sukunimi())
```
```
Pekka
Python
Pauli
Pythonen
```

[Vastaus](osa01-01_hymio/src)
## Lukutilasto
Tässä tehtävässä toteutetaan olio-ohjelmointia hyödyntäen samantapainen käyttäjän syöttämiä lukuja käsittelevä ohjelma kuin Ohjelmoinnin perusteiden osan 2 lopussa.
### Osa 1: Lukujen määrä
Tee luokka Lukutilasto, joka tuntee seuraavat toiminnot:

- metodi lisaa_luku lisää uuden luvun tilastoon
- metodi lukujen_maara kertoo lisättyjen lukujen määrän

Luokan ei tarvitse tallentaa mihinkään lisättyjä lukuja vaan riittää, että se muistaa niiden määrän. Metodin lisaa_luku ei tässä vaiheessa tarvitse edes ottaa huomioon, mikä luku lisätään tilastoon, koska ainoa tallennettava asia on lukujen määrä.

Luokan runko on seuraava:
```
class  Lukutilasto:
    def __init__(self):
        self.lukuja = 0

    def lisaa_luku(self, luku:int):
        pass

    def lukujen_maara(self):
        pass
```
```
tilasto = Lukutilasto()
tilasto.lisaa_luku(3)
tilasto.lisaa_luku(5)
tilasto.lisaa_luku(1)
tilasto.lisaa_luku(2)
print("Lukujen määrä:", tilasto.lukujen_maara())
```
```
Lukujen määrä: 4
```
### Osa 2: Summa ja keskiarvo
Laajenna luokkaa seuraavilla toiminnoilla:

- metodi summa kertoo lisättyjen lukujen summan (tyhjän lukutilaston summa on 0)
- metodi keskiarvo kertoo lisättyjen lukujen keskiarvon (tyhjän lukutilaston keskiarvo on 0)
```
tilasto = Lukutilasto()
tilasto.lisaa_luku(3)
tilasto.lisaa_luku(5)
tilasto.lisaa_luku(1)
tilasto.lisaa_luku(2)
print("Lukujen määrä:", tilasto.lukujen_maara())
print("Summa:", tilasto.summa())
print("Keskiarvo:", tilasto.keskiarvo())
```
```
Määrä: 4
Summa: 11
Keskiarvo: 2.75
```
### Osa 3: Summa käyttäjältä
Tee ohjelma, joka kysyy lukuja käyttäjältä, kunnes käyttäjä antaa luvun -1. Sitten ohjelma ilmoittaa lukujen summan.

Ohjelmassa tulee käyttää Lukutilasto-oliota summan laskemiseen.

HUOM: Älä muuta tässä osassa luokkaa Lukutilasto, vaan toteuta sitä hyödyntäen summan laskemiseen käytetty ohjelma.

HUOM2: Älä kirjoita pääohjelmaa if __name__ == "__main__"-lohkon sisään, jotta testit toimivat!
```
Anna lukuja:
4
2
5
2
-1
Summa: 13
Keskiarvo: 3.25
```
### Osa 4:Monta summaa
Muuta edellistä ohjelmaa niin, että ohjelma laskee myös parillisten ja parittomien lukujen summaa.

HUOM: Älä edelleenkään muuta luokkaa Lukutilasto, vaan määrittele ohjelmassa kolme Lukutilasto-oliota. Laske ensimmäisen avulla kaikkien lukujen summa ja keskiarvo, toisen avulla parillisten lukujen summa ja kolmannen avulla parittomien lukujen summa.

HUOM2: Älä kirjoita pääohjelmaa if __name__ == "__main__"-lohkon sisään, jotta testit toimivat!

Ohjelman tulee toimia seuraavasti:
```
Anna lukuja:
4
2
5
2
-1
Summa: 13
Keskiarvo: 3.25
Parillisten summa: 8
Parittomien summa: 5
```

[Vastaus](osa01-01_hymio/src)
## Sekuntikello
Tehtäväpohjassa on mukana luokan Sekuntikello runko:
```
class Sekuntikello:
    def __init__(self):
        self.sekunnit = 0
        self.minuutit = 0
```
Laajenna luokkaa siten, että se toimii seuraavasti:
```
kello = Sekuntikello()
for i in range(3600):
    print(kello)
    kello.tick()
```
```
00:00
00:01
00:02
... tässä välissä monta riviä
00:59
01:00
01:01
... tässä välissä erittäin monta riviä
59:58
59:59
00:00
00:01
```
Metodi tick vie siis kelloa sekunnin eteenpäin, ja sekä sekuntien että minuuttien arvo on suuruudeltaan korkeintaan 59. Lisäksi oliossa tulee olla metodi __str__, joka näyttää kellonajan yllä olevassa muodossa.

Vihje: metodin tick testailua voi helpottaa asettamalla tilapäisesti konstruktorissa sekunneille ja minuuteille valmiiksi jonkin suuremman arvon kuin 0.

[Vastaus](osa01-01_hymio/src)
## Kello
Toteuta edellistä tehtävää laajentava luokka Kello, joka toimii seuraavaan tapaan:
```
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
```
```
23:59:55
23:59:56
23:59:57
23:59:58
23:59:59
00:00:00
00:00:01
12:05:00
```
Konstruktori siis antaa kellon tunneille, minuuteille ja sekunneille alkuarvot. Metodi tick vie kelloa sekunnin eteenpäin ja metodilla aseta voi asettaa kellon tunneille ja minuuteille uuden arvon ja nollata sekunnit.

[Vastaus](osa01-01_hymio/src)
## Maksukortti
Helsingin Yliopiston opiskelijaruokaloissa eli Unicafeissa opiskelijat maksavat lounaansa käyttäen maksukorttia.

Tässä tehtäväsarjassa tehdään luokka Maksukortti, jonka tarkoituksena on jäljitellä Unicafeissa tapahtuvaa maksutoimintaa.
### Osa 1: Luokan runko
Tee ohjelmaan uusi luokka nimeltä Maksukortti.

Tee ensin luokalle konstruktori, jolle annetaan kortin alkusaldo ja joka tallentaa sen olion sisäiseen muuttujaan. Tee sitten __str__-metodi, joka palauttaa kortin saldon muodossa "Kortilla on rahaa X euroa". Rahamäärä tulee tulostaa yhden desimaalin tarkkuudella.

Seuraavassa on luokan Maksukortti runko:
```
class Maksukortti:
    def __init__(self, alkusaldo: float):
        self.saldo = alkusaldo

    def __str__(self):
        pass
```
Käyttöesimerkki
```
kortti = Maksukortti(50)
print(kortti)
```
Ohjelman tulisi tuottaa seuraava tulostus:
```
Kortilla on rahaa 50.0 euroa
```
### Osa 2: Kortilla maksaminen
Täydennä Maksukortti-luokkaa seuraavilla metodeilla:

- syo_edullisesti joka vähentää kortin saldoa 2.60 eurolla
- syo_maukkaasti joka vähentää kortin saldoa 4.60 eurolla
Seuraava pääohjelma testaa luokkaa
```
kortti = Maksukortti(50)
print(kortti)

kortti.syo_edullisesti()
print(kortti)

kortti.syo_maukkaasti()
kortti.syo_edullisesti()
print(kortti)
```
Ohjelman tulisi tuottaa seuraava tulostus:
```
Kortilla on rahaa 50.0 euroa
Kortilla on rahaa 47.4 euroa
Kortilla on rahaa 40.2 euroa
```
Huomaa, että kortin saldo ei saa mennä negatiiviseksi:
```
kortti = Maksukortti(4)
print(kortti)

kortti.syo_edullisesti()
print(kortti)

kortti.syo_edullisesti()
print(kortti)
```
```
Kortilla on rahaa 4.0 euroa
Kortilla on rahaa 1.4 euroa
Kortilla on rahaa 1.4 euroa
```
Eli kortin saldo ei enää vähene jos maksettaessa saldo ei ole riittävä.
### Osa 3: Kortin lataaminen
Lisää Maksukortti-luokkaan metodi lataa_rahaa.

Metodin tarkoituksena on kasvattaa kortin saldoa parametrina annetulla rahamäärällä.
```
kortti = Maksukortti(10)
print(kortti)
kortti.lataa_rahaa(15)
print(kortti)
kortti.lataa_rahaa(10)
print(kortti)
kortti.lataa_rahaa(200)
print(kortti)
```
```
Kortilla on rahaa 10.0 euroa
Kortilla on rahaa 25.0 euroa
Kortilla on rahaa 35.0 euroa
Kortilla on rahaa 235.0 euroa
```
Jos kortille yritetään ladata negatiivinen summa, tulee metodin tuottaa poikkeus ValueError:
```
kortti = Maksukortti(10)
kortti.lataa_rahaa(-10)
```
```
File "testi.py", line 3, in maksukortti
ValueError: Kortille ei saa ladata negatiivista summaa
```
Huomaa että metodin tulee tuottaa poikkeus, katso osan 6 materiaalista miten poikkeus tuotetaan. Metodi ei missään tilanteessa itse tulosta mitään!
### Osa 4: Monta korttia
Tee pääohjelma, joka sisältää seuraavan tapahtumasarjan:

- Luo Pekan kortti. Kortin alkusaldo on 20 euroa
- Luo Matin kortti. Kortin alkusaldo on 30 euroa
- Pekka syö maukkaasti
- Matti syö edullisesti
- Korttien arvot tulostetaan (molemmat omalle rivilleen, rivin alkuun kortin omistajan nimi)
- Pekka lataa rahaa 20 euroa
- Matti syö maukkaasti
- Korttien arvot tulostetaan (molemmat omalle rivilleen, rivin alkuun kortin omistajan nimi)
- Pekka syö edullisesti
- Pekka syö edullisesti
- Matti lataa rahaa 50 euroa
- Korttien arvot tulostetaan (molemmat omalle rivilleen, rivin alkuun kortin omistajan nimi)

Pääohjelman runko
```
pekan_kortti = Maksukortti(20)
matin_kortti = Maksukortti(30)
# tee koodi tänne
```
Tulostuksen tulee olla seuraava
```
Pekka: Kortilla on rahaa 15.4 euroa
Matti: Kortilla on rahaa 27.4 euroa
Pekka: Kortilla on rahaa 35.4 euroa
Matti: Kortilla on rahaa 22.8 euroa
Pekka: Kortilla on rahaa 30.2 euroa
Matti: Kortilla on rahaa 72.8 euroa
```

[Vastaus](osa01-01_hymio/src)
## Sarja
### Osa 1: Luokka Sarja
Tee luokka Sarja, joka toimii seuraavasti
```
dexter = Sarja("Dexter", 8, ["Crime", "Drama", "Mystery", "Thriller"])
print(dexter)
```
```
Dexter (8 esityskautta)
genret: Crime, Drama, Mystery, Thriller
ei arvosteluja
```
Konstruktorissa siis asetetaan sarjan nimi, sen esityskausien lukumäärä sekä lista, joka kertoo mitä genrejä sarja edustaa.

Vihje: merkkijonotaulukko saadaan muutettua haluttuja välimerkkejä sisältäväksi merkkijonoksi metodin join avulla seuraavasti:
```
lista = ["Crime", "Drama", "Mystery", "Thriller"]
merkkijono = ", ".join(lista)
print(merkkijono)
```
```
Crime, Drama, Mystery, Thriller
```
### Osa 2: Arvostelujen lisääminen
Tee luokalle metodi arvostele(arvosana: int), jonka avulla sarjalle voi lisätä arvosanan, joka on kokonaisluku väliltä 0–5. Myös metodia __str__ tulee muuttaa niin, että se antaa arvostelujen määrän ja keskiarvon pyöristettynä yhden desimaalin tarkkuudelle (jos arvosteluja on annettu).
```
dexter = Sarja("Dexter", 8, ["Crime", "Drama", "Mystery", "Thriller"])
dexter.arvostele(4)
dexter.arvostele(5)
dexter.arvostele(5)
dexter.arvostele(3)
dexter.arvostele(0)
print(dexter)
```
```
Dexter (8 esityskautta)
genret: Crime, Drama, Mystery, Thriller
arvosteluja 5, keskiarvo 3.4 pistettä
```
### Osa 3: Sarjojen haku
Tee kaksi funktiota arvosana_vahintaan(arvosana: float, sarjat: list) ja sisaltaa_genren(genre: str, sarjat: list), joiden avulla on mahdollista etsiä listalla olevia sarjoja.

Metodit toimivat seuraavasti:
```
s1 = Sarja("Dexter", 8, ["Crime", "Drama", "Mystery", "Thriller"])
s1.arvostele(5)

s2 = Sarja("South Park", 24, ["Animation", "Comedy"])
s2.arvostele(3)

s3 = Sarja("Friends", 10, ["Romance", "Comedy"])
s3.arvostele(2)

sarjat = [s1, s2, s3]

print("arvosana vähintään 4.5:")
for sarja in arvosana_vahintaan(4.5, sarjat):
    print(sarja.nimi)

print("genre Comedy:")
for sarja in sisaltaa_genren("Comedy", sarjat):
    print(sarja.nimi)
```
```
arvosana vähintään 4.5:
Dexter

genre Comedy:
South Park
Friends
```
Huomaa, että yllä oleva koodi ja testit olettavat, että luokassa on attribuutti nimi. Jos olet käyttänyt muuta nimeä, sinun kannattaa vaihtaa se nyt.

[Vastaus](osa01-01_hymio/src)
