# ----------------------------------------------------------------------
# B1. Servisi, kas darbojas
# ----------------------------------------------------------------------

# Izvadi tikai tos servisus, kuru statuss ir Running, sakārtotus pēc nosaukuma.
# Aizpildi vietu, kur stāv TODO.

Get-Service |
    # TODO: atlasi tikai tos, kuru Status ir Running
    Where-Object { $_.Status -eq 'Running' } |
    Sort-Object Name |
    Select-Object Name, Status
