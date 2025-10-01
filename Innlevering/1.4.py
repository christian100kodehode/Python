#Oppgave 1.4
#Lag et program som bytter plass på to elementer i en gitt liste. Programmet
#skal ta utgangspunkt i følgende liste:
#fruits = ["eple", "banan", "appelsin", "drue", "kiwi"]
#1. Be brukeren om ˚a skrive inn to indekser (input) som angir hvilke
#elementer i listen som skal bytte plass
#2. Bytt plass på elementene som ligger på de angitte indeksene
#3. Skriv ut den oppdaterte listen
#Hvis en eller begge indeksene er ugyldige (ikke i listen), skal programmet gi
#en passende feilmelding
fruits = ["eple", "banan", "appelsin", "drue", "kiwi"]
print(f"Original order:\n{fruits}\n")
fruits_length = len(fruits) - 1

while True:
    try:
        fruit1 = int(input("Skriv inn indeks på første frukt som skal stokkes om (0 - 4 ):"))
        fruit2 = int(input("Skriv inn indeks på andre frukt som skal stokkes om (0 - 4):"))
        if fruit1 > fruits_length:
            print(f"Enter a valid number from 0 to {fruits_length}\n")
            continue
        if fruit2 > fruits_length:
            print(f"Enter a valid number from 0 to {fruits_length}\n")
            continue
        if fruit1 == fruit2:
            print("Enter two differen numbers please.")
            continue
        fruits[fruit1], fruits[fruit2] = fruits[fruit2], fruits[fruit1]
    except ValueError:
        print(f"Enter a valid number from 0 to {fruits_length}\n")
    except IndexError:
        print(f"Enter a valid number from 0 to {fruits_length}\n")
    else:
        break

print(f"Swapped order as requested is (swap position {fruit1} with {fruit2})\nResulting in:\n{fruits}.")