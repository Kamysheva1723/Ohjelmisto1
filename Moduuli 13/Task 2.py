"""
Toteuta taustapalvelu, joka palauttaa annettua lentokentän ICAO-koodia vastaavan lentokentän nimen
ja kaupungin JSON-muodossa. Tiedot haetaan opintojaksolla käytetystä lentokenttätietokannasta.
Esimerkiksi EFHK-koodia vastaava GET-pyyntö annetaan muodossa: http://127.0.0.1:3000/kenttä/EFHK.
Vastauksen on oltava muodossa: {"ICAO":"EFHK", "Name":"Helsinki Vantaa Airport", "Municipality":"Helsinki"}.
"""
#for task2
import mysql.connector
import json
from flask import Flask, Response


app = Flask(__name__)

def get_data_from_db(code):
    yhteys = mysql.connector.connect(
        host='127.0.0.1',
        port=3306,  # MariaDB port
        database='flight_game',
        user='userN',
        password='1234',
        autocommit=True)

    sql = "select airport.name, airport.municipality from airport where ident = '" + code + "'"

    kursori = yhteys.cursor()
    kursori.execute(sql)
    tulos = kursori.fetchone()
    yhteys.close()

    return tulos

@app.route('/kenttä/<code>')
def kenttä(code):

    try:
        tulos = get_data_from_db(code)
        if tulos:
            tilakoodi = 200
            vastaus = {
                "status": tilakoodi,
                "ICAO": code,
                "Name": tulos[0],
                "Municipality": tulos[1]
            }
        else:
            tilakoodi = 200
            vastaus = {
                "status": tilakoodi,
                "ICAO": code,
                "Name": "not found",
                "Municipality": "not found"
            }

    except ValueError:
        tilakoodi = 400
        vastaus = {
            "status": tilakoodi,
            "teksti": "Virheellinen yhteenlaskettava"
        }

    jsonvast = json.dumps(vastaus)
    return Response(response=jsonvast, status=tilakoodi, mimetype="application/json")

@app.errorhandler(404)
def page_not_found(virhekoodi):
    vastaus = {
        "status" : "404",
        "teksti" : "Virheellinen päätepiste"
    }
    jsonvast = json.dumps(vastaus)
    return Response(response=jsonvast, status=404, mimetype="application/json")

if __name__ == '__main__':
    app.run(use_reloader=True, host='127.0.0.1', port=3000)





