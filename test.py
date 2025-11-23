def print_tabell_enkel(m, n):
    """
    Skriver ut en enkel, formatert tabell for et tallintervall [m, n].
    """
    if m > n:
        print("Advarsel: 'm' må være mindre enn eller lik 'n'.")
        return

    # Skriver ut tabelloverskriften
    print(f"{'Tall':<10}{'Kvadrat':<10}{'Kube':<10}")
    print("-" * 30)

    # Itererer gjennom intervallet og skriver ut hver rad
    for tall in range(m, n + 1):
        kvadrat = tall ** 2
        kube = tall ** 3
        print(f"{tall:<10}{kvadrat:<10}{kube:<10}")

# Angi et intervall [m, n]
start = 1
slutt = 11

# Skriv ut tabellen
print_tabell_enkel(start, slutt)