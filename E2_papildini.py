# ----------------------------------------------------------------------
# E2. CSV atskaite
# ----------------------------------------------------------------------

# Saglabā līmeņu kopsavilkumu CSV failā, ko var atvērt Excel ar latviešu burtiem.
# Aizpildi vietu, kur stāv TODO.

import csv

skaits = {"INFO": 747, "WARNING": 284, "ERROR": 146, "CRITICAL": 23}

# TODO: ieraksti skaits saturu failā limeni.csv
# Divas kolonnas: Līmenis un Skaits

with open("limeni.csv", mode="w", encoding="utf-8-sig", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["Līmenis", "Skaits"])
    for limenis, vertiba in skaits.items():
        writer.writerow([limenis, vertiba])
