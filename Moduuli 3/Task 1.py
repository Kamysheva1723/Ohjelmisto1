"""
Kirjoita ohjelma, joka kysyy kalastajalta kuhan pituuden senttimetreinä.
Jos kuha on alamittainen, ohjelma käskee laskea kuhan takaisin järveen ilmoittaen samalla käyttäjälle,
montako senttiä alimmasta sallitusta pyyntimitasta puuttuu.
Kuha on alamittainen, jos sen pituus on alle 37 cm.
"""

KuhanPituus = float(input("Anna kuhan pituuden senttimetreinä: "))
if KuhanPituus < 37:
    print(f"Laskee kuhasi takaisin järveen, sen täytty kasvaa vielä {37 - KuhanPituus} cm.")