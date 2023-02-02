"""
Kirjoita ohjelma, joka kysyy käyttäjältä lentoaseman ICAO-koodin.
Ohjelma hakee ja tulostaa koodia vastaavan lentokentän nimen ja sen sijaintikunnan kurssilla
käytettävästä lentokenttätietokannasta. ICAO-koodi on tallennettuna airport-taulun ident-sarakkeeseen.

Valitse PyCharmissa View/Tools Windows/Python Packages.
Kirjoita hakukenttään hakusanaksi connector ja etsi luettelosta vaihtoehto mysql-connector-python.
Napsauta kyseistä vaihtoehtoa ja paina Install.
"""

import mysql.connector

yhteys = mysql.connector.connect(
         host='127.0.0.1',  #localhost
         port=3306,         #MariaDB port
         database='flight_game',
         user='userN',
         password='1234',
         autocommit=True)       #меняется немедленно

ident = input("Anna ICAO - koodi: ")

sql = "select airport.name, country.name  from airport, country " \
      "where ident = '" + ident + "' and airport.iso_country = country.iso_country"

#print (sql)

kursori = yhteys.cursor()
kursori.execute(sql)
tulos = kursori.fetchall()

print (tulos)

#suljetaan yhteys
yhteys.close()




