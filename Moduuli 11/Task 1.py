"""
Toteuta seuraava luokkahierarkia Python-kielellä: Julkaisu voi olla kirja tai lehti.
Jokaisella julkaisulla on nimi. Kirjalla on lisäksi kirjoittaja ja sivumäärä,
kun taas lehdellä on päätoimittaja. Kirjoita luokkiin myös tarvittavat alustajat.
Tee aliluokkiin metodi tulosta_tiedot, joka tudostaa kyseisen julkaisun kaikki tiedot.
Luo pääohjelmassa julkaisut Aku Ankka (päätoimittaja Aki Hyyppä) ja Hytti n:o 6
(kirjailija Rosa Liksom, 200 sivua). Tulosta molempien julkaisujen kaikki tiedot toteuttamiesi
metodien avulla.
"""


class Publication:
    def __init__(self, title):
        self.title = title


class Book(Publication):
    def __init__(self, title, author, page_number):
        Publication.__init__(self,title)
        self.author = author
        self.page_number = page_number


class Magazine(Publication):
    def __init__(self, title, editor):
        Publication.__init__(self,title)
        self.editor = editor



duck_mag = Magazine("Aku Ankka", "Aki Hyyppä")
train_book = Book("Hytti n:o 6","Rosa Liksom",200)
print(f"Lehden nimi on {duck_mag.title} ja sen päätoimittaja on {duck_mag.editor}.")
print(f"Kirjan nimi on {train_book.title} ja sen kirjailija on {train_book.author}, siinä on {train_book.page_number} sivua.")