"""
Kirjoita ohjelma, joka arpoo ja tulostaa kaksi erilaista numerolukon koodia:
kolmenumeroisen koodin, jonka kukin numeromerkki on väliltä 0..9.
nelinumeroisen koodin, jonka kukin numeromerkki on väliltä 1..6.
Vihje: tutustu random.randint()-funktion käyttöön.
"""
import random

print(f"Satunnainen kolminumeroinen koodi on "
      f"{random.randint(0,9)}"
      f"{random.randint(0,9)}"
      f"{random.randint(0,9)}.")

print(f"Satunnainen nelinumeroinen koodi on "
      f"{random.randint(0,6)}"
      f"{random.randint(0,6)}"
      f"{random.randint(0,6)}"
      f"{random.randint(0,6)}.")
