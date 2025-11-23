#Oppgave 2.6
#Konverter datasettet fra Oppgave 2.2 til en liste av dictionaries med formatet:
#{"navn": "Cecilie", "alder": 28}

Name_age_list = ["Cecilie", 28, "Bjørn", 30, "Tor", 24, "Anna", 25]

#Empty list to store inside
list_of_dicts = []
#loop through, step of 2
for i in range(0, len(Name_age_list), 2):
    #create dictioanry with name and age for each pair
    person_dict = {"navn": Name_age_list[i], "alder": Name_age_list[i + 1]}
    list_of_dicts.append(person_dict)

print(list_of_dicts)