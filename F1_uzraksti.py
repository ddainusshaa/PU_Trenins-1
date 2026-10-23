# ----------------------------------------------------------------------
# F1. Rīks ar argumentu
# ----------------------------------------------------------------------

# Uzraksti skriptu, kuram meklējamo kļūdas līmeni padod kā argumentu komandrindā. Skripts izvada, cik tāda līmeņa rindu žurnālā ir un parāda pirmās trīs no tām. Ja arguments nav padots, skripts izvada pamācību un neavarē.
import sys

if len(sys.argv) < 2:
    print("Noradi aguemtnu piemeram, python script.py ERROR)")
    sys.exit()

mekletais_limenis = sys.argv[1]
skaits = 0
pirmas_rindas = []

try:
    with open("sistema.log", encoding="utf-8") as f:
        for rinda in f:
            dalas = rinda.split()
            if len(dalas) > 2 and dalas[2] == mekletais_limenis:
                skaits += 1
                if len(pirmas_rindas) < 3:
                    pirmas_rindas.append(rinda.strip())

    print(f"Kopejais rindu skaits ar limeni {mekletais_limenis}: {skaits}")
    for r in pirmas_rindas:
        print(r)

except FileNotFoundError:
    print("Fails 'sistema.log' netika atrasts")
