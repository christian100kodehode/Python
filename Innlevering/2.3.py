#Oppgave 2.3
#Ta utgangspunkt i listene fra Oppgave 2.2 og lag en dictionary der tekstverdier
#fra listen med navn blir nøkler og tallverdiene fra listen med alder blir
#verdier. Skriv ut innholdet av denne dictionary på formatet:
#"Cecilie er 25 år"
#"Bjørn er 30 år"


# # All is in assignment 2.2 now




# --------- NEW

name_age_list = ["Cecilie", 28, "Bjørn", 30, "Tor", 24, "Anna", 25]
name_list = []
age_list = []
# make split doing step 2, start position 0 in list
name_list = name_age_list[::2]
# make split doing step 2, start position 1 in list
age_list = name_age_list[1::2]
# print the two lists
print(" ")
print("Two lists seperating the values from initial list:")
print(f"Navn: {name_list}")
print(f"Alder: {age_list}")

# make dictionary from the 2 lists
name_age_dict = dict(zip(name_list, age_list))
# loop thruogh and add text for values in dictionary:
print(" ")
print("Dictionary with added text between key and value for contents:")
for key, value in name_age_dict.items():
    print(f"{key} er {value} år.")

# make sorted list of tuples from dictionary with pairs (name, age)
print(" ")
sorted_list_age = sorted(name_age_dict.items(), key=lambda item: item[1], reverse=True)
# create new dictionary from sorted list with values (name, age)
sorted_age_dict = {name: age for name, age in sorted_list_age}
print("Print of dictionary sorted by age:")
print(sorted_age_dict)

# list from dictionary sorted by name, alphabetical
print(" ")
# loop through dictionary. sorter alfabetisk og lag sortert liste
sorted_name_list = []
for key in sorted(sorted_age_dict):
    sorted_name_list.append(key)
    sorted_name_list.append(sorted_age_dict[key])
print("Print of list sorted by name:")
print(sorted_name_list)


# Make list of dictionaries from original name_age_list from assignment 2.2
print(" ")
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

# my_dict = {"Cecilie": {"age": 28},"Bjørn": {"age": 30},"Tor": {"age": 24},"Anna": {"age": 25}}

#loop igjennom og legg til navn som nøkkel og alder som verdi

# for names in my_dict:
#     for word, number in my_dict[names].items():
#         print(names ,"er" ,number , "år.")
# ___________________________________________