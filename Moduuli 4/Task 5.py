"""
Kirjoita ohjelma, joka kysyy käyttäjältä käyttäjätunnuksen ja salasanan.
Jos jompikumpi tai molemmat ovat väärin,
tunnus ja salasana kysytään uudelleen.
Tätä jatketaan kunnes kirjautumistiedot ovat oikein tai väärät tiedot on syötetty viisi kertaa.
Edellisessä tapauksessa tulostetaan Tervetuloa ja jälkimmäisessä Pääsy evätty.
(Oikea käyttäjätunnus on python ja salasana rules).
"""
UserName_original = "python"
Password_original = "rules"

counter = 1
Message = "Pääsy evätty."

while counter <=5 and Message != "Tervetuloa!":
    UserName = input("Anna käyttäjätunnus: ")
    Password = input("Anna salasana: ")
    if UserName_original != UserName or Password_original != Password:
        print ("Virheellinen käyttäjätunnus ja/tai salasana syötetty.")
    else:
        Message = "Tervetuloa!"
    counter += 1

print (f"{Message}")


