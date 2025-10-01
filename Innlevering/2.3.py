#Oppgave 2.3
#Ta utgangspunkt i listene fra Oppgave 2.2 og lag en dictionary der tekstverdier
#fra listen med navn blir nøkler og tallverdiene fra listen med alder blir
#verdier. Skriv ut innholdet av denne dictionary på formatet:
#"Cecilie er 25 år"
#"Bjørn er 30 år"

my_dict = {"Cecilie": {"age": 28},"Bjørn": {"age": 30},"Tor": {"age": 24},"Anna": {"age": 25}}

#loop igjennom og legg til navn som nøkkel og alder som verdi
for names in my_dict:
    for word, number in my_dict[names].items():
        print(names ,"er" ,number , "år.")
