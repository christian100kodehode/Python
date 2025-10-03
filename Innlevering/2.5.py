#Oppgave 2.5
#Ta utgangspunktet i dictionary som er sortert på navn i Oppgave 2.4 og
#lag en ny liste med disse verdiene slik at listen får samme format som den i
#Oppgave 2.2, men sortert på navn.
#["Anna", 25, "Bjørn", 30, "Cecilie", 28, "Tor", 24]

my_dict = {"Cecilie": {"age": 28},"Bjørn": {"age": 30},"Tor": {"age": 24},"Anna": {"age": 25}}

#items() to return the key value in the dictionary, with a lambda function to access the name, sort by name alphabetically.
sorted_dict = dict(sorted(my_dict.items(), key=lambda x: x[0]))

print(sorted_dict)