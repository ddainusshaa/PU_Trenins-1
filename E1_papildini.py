# ----------------------------------------------------------------------
# E1. Kļūdas pa servisiem
# ----------------------------------------------------------------------

# Saskaiti, cik ERROR rindu ir katram servisam, un izvadi tos no biežākā uz retāko.
# Aizpildi vietu, kur stāv TODO.

skaits = {}

with open("sistema.log", encoding="utf-8") as f:
    for rinda in f:
        dalas = rinda.split()
        if dalas[2] == "ERROR":
            serviss = dalas[3].rstrip(":")
            # TODO: pieskaiti vienu šim servisam
            skaits[serviss] = skaits.get(serviss, 0) + 1

# TODO: izvadi sakārtotus no lielākā uz mazāko

for serviss, count in sorted(skaits.items(), key=lambda item: item[1], reverse=True):
    print(f"{serviss}: {count}")
