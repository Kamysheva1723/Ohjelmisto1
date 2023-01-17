"""
Kirjoita ohjelma, joka kysyy käyttäjän biologisen sukupuolen ja hemoglobiiniarvon (g/l).
Ohjelma ilmoittaa, onko hemoglobiiniarvo alhainen, normaali vai korkea.

Naisen normaali hemoglobiiniarvo on välillä 117-175 g/l.
Miehen normaali hemoglobiiniarvo on välillä 134-195 g/l.
"""

SukuPuoli = input ("Anna sinun sukupuolisi (M tai N): ")
hemArvo = float(input ("Anna sinun hemoglobiinarvon (g/l): "))

if SukuPuoli == "M" or SukuPuoli == "m":
    if hemArvo < 134:
        print ("Sinun gemoglobiinarvon on alhainen miehelle.")
    elif hemArvo > 195:
        print("Sinun gemoglobiinarvon on korkea miehelle.")
    else:
        print("Sinulla on normaali gemoglobiinarvoa.")
# naiset
elif hemArvo < 117 and (SukuPuoli == "N" or SukuPuoli == "n"):
    print ("Sinun gemoglobiinarvon on alhainen naisille.")
elif hemArvo > 175 and (SukuPuoli == "N" or SukuPuoli == "n"):
    print("Sinun gemoglobiinarvon on korkea naisille.")
elif SukuPuoli == "N" or SukuPuoli == "n":
    print("Sinulla on normaali gemoglobiinarvoa.")
else:
    print ("Virheellinen sukupuoli.")
