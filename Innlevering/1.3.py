#Oppgave 1.3
#Lag et program som ber brukeren skrive inn et tall og genererer multiplikasjonstabellen
#for dette tallet (fra 1 til 10). Eksempel:
#Input: 3
#Output:
#3 * 1
#3 * 2
#3 * 3
#Osv.

print("Enter a number to see the multiplication to 10.\n")
while True:
    try:
        user_input_number = input("Enter number here:")
        selected_number = int(user_input_number)
        # Loop throug, from - to
        for i in range(1, 11):
            result = selected_number * i
            print(f"{selected_number} x {i} = {result}") 
    except ValueError:
        print("Try again, only numbers allowed.")
    else:
        break