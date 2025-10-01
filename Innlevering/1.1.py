#1 Grunnprogrammering
#
#Oppgave 1.1
#Lag et program som ber brukeren om å skrive inn et positivt heltall (int)
#og finner summen av alle tall fra 1 til dette tallet (inkluder også tallet i
#summen). Summen skal beregnes ved hjelp av en for-løkke.


#Ask for a integer and a number that is larger and not equal to 0, if not run again untill succesful input.
while True:
    try:
        user_input_number = input("Enter a positive whole number here:")
        selected_number = int (user_input_number) 
        if selected_number <= 0:
            print("Enter a positive number/not zero, please.")
            continue
    except ValueError:
        print("Try again, no decimal numbes or letters allowed. Only whole numbers.")
    else:
        print(f"Thank you, you entered: {user_input_number}")
        break

#sum all numbers from 1 inclduing to selected and print result:
sum_all_numbers = 0
for i in range(1, selected_number + 1):
   sum_all_numbers += i
 
print(f"\nAll numbers added up from 1 including the entered value is\n\n in total: {sum_all_numbers}")