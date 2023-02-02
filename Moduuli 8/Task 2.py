"""
Kirjoita ohjelma, joka kysyy käyttäjältä maakoodin (esimerkiksi FI) ja tulostaa
kyseisessä maassa olevien lentokenttien lukumäärät tyypeittäin.
Esimerkiksi Suomen osalta tuloksena on saatava tieto siitä, että pieniä lentokenttiä
on 65 kappaletta, helikopterikenttiä on 15 kappaletta jne.
"""

import mysql.connector

yhteys = mysql.connector.connect(
         host='127.0.0.1',  #localhost
         port=3306,         #MariaDB port
         database='flight_game',
         user='userN',
         password='1234',
         autocommit=True)       #меняется немедленно

ident = input("Anna ICAO - maakoodi: ")

sql =   "select type, count(*) from airport " \
        "where iso_country = '" + ident + "' " \
        "group by type";

#print (sql)

kursori = yhteys.cursor()
kursori.execute(sql)
tulos = kursori.fetchall()

print (tulos)

#suljetaan yhteys
yhteys.close()