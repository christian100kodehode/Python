#Oppgave 2.2
#Ta utgangspunkt i en liste der tekst og tall er plassert parvis med navn og
#alder slik:
#["Cecilie", 28, "Bjørn", 30, "Tor", 24, "Anna", 25]
#Skriv et program som splitter denne listen i to separert lister, en liste for
#navn og en liste for alder.

Name_age_list = ["Cecilie", 28, "Bjørn", 30, "Tor", 24, "Anna", 25]
string_list = " ".join(map(str, Name_age_list))

print("Now all names and numbers are in a string with space seperating them.")
print(string_list)

names = ""
numbers = ""

#loop through the list
for i in string_list:
    # if letter or space add to names
    if i.isalpha() or i.isspace():
        names += i
    # if number or space add to numbers
    if i.isdigit() or i.isspace():
        numbers += i

#split names into list, remove added spaces
clean_names = names.split()
clean_numbers = numbers.split()

print(f"\nList of only names {clean_names}.")
print(f"List of only numbers {clean_numbers}.")
