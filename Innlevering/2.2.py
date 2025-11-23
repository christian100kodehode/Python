#Oppgave 2.2
#Ta utgangspunkt i en liste der tekst og tall er plassert parvis med navn og
#alder slik:
#["Cecilie", 28, "Bjørn", 30, "Tor", 24, "Anna", 25]
#Skriv et program som splitter denne listen i to separert lister, en liste for
#navn og en liste for alder.


# --------- NEW Assignment 2.2 - 2.6

name_age_list = ["Cecilie", 28, "Bjørn", 30, "Tor", 24, "Anna", 25]
name_list = []
age_list = []
# make split doing step 2, start position 0 in list
name_list = name_age_list[::2]
# make split doing step 2, start position 1 in list
age_list = name_age_list[1::2]
# print the two lists
print(" ")
print("Assignment 2.2")
print("Two lists seperating the values from initial list:")
print(f"Navn: {name_list}")
print(f"Alder: {age_list}")

# make dictionary from the 2 lists
name_age_dict = dict(zip(name_list, age_list))
# loop thruogh and add text for values in dictionary:
print(" ")
print("Assignment 2.3")
print("Dictionary with added text between key and value for contents:")
for key, value in name_age_dict.items():
    print(f"{key} er {value} år.")

# make sorted list of tuples from dictionary with pairs (name, age)
print(" ")
print("Assignment 2.4")
sorted_list_age = sorted(name_age_dict.items(), key=lambda item: item[1], reverse=True)
# create new dictionary from sorted list with values (name, age)
sorted_age_dict = {name: age for name, age in sorted_list_age}
print("Print of dictionary sorted by age:")
print(sorted_age_dict)

# list from dictionary sorted by name, alphabetical
print(" ")
print("Assignment 2.5")
# loop through dictionary. sorter alfabetisk og lag sortert liste
sorted_name_list = []
for key in sorted(sorted_age_dict):
    sorted_name_list.append(key)
    sorted_name_list.append(sorted_age_dict[key])
print("Print of list sorted by name:")
print(sorted_name_list)


# Make list of dictionaries from original name_age_list from assignment 2.2
print(" ")
print("Assignment 2.6")
list_of_dicts = []
#loop through, step of 2
for i in range(0, len(name_age_list), 2):
    #create dictioanry with name and age for each pair
    person_dict = {"navn": name_age_list[i], "alder": name_age_list[i + 1]}
    list_of_dicts.append(person_dict)
print("List of dictionaries from original name_age_list:")
print(list_of_dicts)





# ___________________________________________
# OLD CODE FROM TRY 1:
# Name_age_list = ["Cecilie", 28, "Bjørn", 30, "Tor", 24, "Anna", 25]
# string_list = " ".join(map(str, Name_age_list))

# print("Now all names and numbers are in a string with space seperating them.")
# print(string_list)

# names = ""
# numbers = ""

#loop through the list

# for i in string_list:
    # if letter or space add to names

    # if i.isalpha() or i.isspace():
    #     names += i
    # if number or space add to numbers

    # if i.isdigit() or i.isspace():
    #     numbers += i

#split names into list, remove added spaces

# clean_names = names.split()
# clean_numbers = numbers.split()

# print(f"\nList of only names {clean_names}.")
# print(f"List of only numbers {clean_numbers}.")

# ___________________________________________