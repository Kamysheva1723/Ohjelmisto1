"""
Kirjoita ohjelma, joka kysyy käyttäjältä kahden lentokentän ICAO-koodit.
Ohjelma ilmoittaa lentokenttien välisen etäisyyden kilometreinä.
Laskenta perustuu tietokannasta haettuihin koordinaatteihin.
Laske etäisyys geopy-kirjaston avulla: https://geopy.readthedocs.io/en/stable/.
Asenna kirjasto valitsemalla View / Tool Windows / Python Packages.
Kirjoita hakukenttään geopy ja vie asennus loppuun.
"""
from geopy import distance
import mysql.connector


l1_ident = input ("Anna ensimasen lentoaseman ICAO - koodi: ")
l2_ident = input ("Anna toisen lentoaseman ICAO - koodi: ")

yhteys = mysql.connector.connect(
         host='127.0.0.1',  #localhost
         port=3306,         #MariaDB port
         database='flight_game',
         user='userN',
         password='1234',
         autocommit=True)       #меняется немедленно

sql1 =   "select latitude_deg, longitude_deg from airport " \
         "where ident = '" + l1_ident + "'";

sql2 =   "select latitude_deg, longitude_deg from airport " \
         "where ident = '" + l2_ident + "'";

#print (sql1, sql2)

kursori = yhteys.cursor()

kursori.execute(sql1)
lentoasema1 = kursori.fetchall()

kursori.execute(sql2)
lentoasema2 = kursori.fetchall()

#print (lentoasema1, lentoasema2)
#EFKU kuopio EFHK helsinki

from geopy import distance

print(distance.distance(lentoasema1, lentoasema2))
#suljetaan yhteys
yhteys.close()

