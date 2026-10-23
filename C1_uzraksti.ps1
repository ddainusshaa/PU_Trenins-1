# ----------------------------------------------------------------------
# C1. Atskaite par procesoru
# ----------------------------------------------------------------------

# Uzraksti PowerShell skriptu, kas izvada desmit procesus ar lielāko procesora patēriņu (CPU) un saglabā tos CSV failā. Katrai rindai jābūt procesa nosaukumam, CPU un atmiņai.

Get-Process | Sort-Object CPU -Descending | Select-Object -First 10 Name, CPU, WorkingSet | Export-Csv -Path cpu_atskaite.csv -NoTypeInformation
