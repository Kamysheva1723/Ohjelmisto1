"""
Kirjoita ohjelma, joka kysyy käyttäjältä kuukauden numeron, jonka jälkeen ohjelma tulostaa sitä
vastaavan vuodenajan (kevät, kesä, syksy, talvi). Tallenna ohjelmassasi kuukausia vastaavat vuodenajat
merkkijonoina monikkotietorakenteeseen. Määritellään kukin vuodenaika kolmen kuukauden mittaiseksi siten,
että joulukuu on ensimmäinen talvikuukausi.
"""
VuodenAjat = ("talvi","kevät","kesä","syksy")
TalvenKk = (12,1,2)
KevätKk = (3,4,5)
KesäKk = (6,7,8)
SyksyKk = (9,10,11)

month = int (input ("Anna kuukauden numeron: "))

if month in TalvenKk:
    print (f"{month}. kuukausi kuuluu vuodenaikaan ´{VuodenAjat[0]}´")
elif month in KevätKk:
    print (f"{month}. kuukausi kuuluu vuodenaikaan ´{VuodenAjat[1]}´")
elif month in KesäKk:
    print (f"{month}. kuukausi kuuluu vuodenaikaan ´{VuodenAjat[2]}´")
elif month in SyksyKk:
    print (f"{month}. kuukausi kuuluu vuodenaikaan ´{VuodenAjat[3]}´")