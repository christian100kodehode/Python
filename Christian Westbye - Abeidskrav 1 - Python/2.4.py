#Oppgave 2.4
#Skriv et program som sorterer denne dictionary etter alder hvor den eldste
#skal være først. Skriv ut resultatet.

my_dict = {"Cecilie": {"age": 28},"Bjørn": {"age": 30},"Tor": {"age": 24},"Anna": {"age": 25}}

#items() to return the key value in a dictionary sort with a lambda function to access the age key in the nested dictionary, reverse to get the oldest first.
sorted_dict = dict(sorted(my_dict.items(), key=lambda x: x[1]["age"], reverse=True))

print(sorted_dict)