"""
Toteuta Flask-taustapalvelu, joka ilmoittaa, onko parametrina saatu luku alkuluku vai ei.
Hyödynnä toteutuksessa aiempaa tehtävää, jossa alkuluvun testaus tehtiin.
Esimerkiksi lukua 31 vastaava GET-pyyntö annetaan muodossa: http://127.0.0.1:3000/alkuluku/31.
Vastauksen on oltava muodossa: {"Number":31, "isPrime":true}.
"""
from flask import Flask, Response
import json

app = Flask(__name__)

@app.route('/alkuluku/<luku>')
def alkuluku(luku):

    try:
        luku = int(luku)
        # Jos luku on pariton, se ei ole jaollinen parillisilla luvuilla.
        if luku % 2 != 0:
            Step = 2
            d = 3
        else:
            Step = 1
            d = 2

        # d on pienin jakaja, joka ei voi olla suurempi kuin annetun luvun neliöjuuri
        while d * d <= luku and luku % d != 0:
            d += Step

        tilakoodi = 200
        if luku == 1:
            vastaus = {
                "status": tilakoodi,
                "Number": luku,
                "isPrime": False
            }
        elif d * d > luku:
            vastaus = {
                "status": tilakoodi,
                "Number": luku,
                "isPrime": True
                }
        else:
            tilakoodi = 200
            vastaus = {
                "status": tilakoodi,
                "Number": luku,
                "isPrime": False
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