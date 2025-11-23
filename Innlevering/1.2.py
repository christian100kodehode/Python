#Oppgave 1.2
#Skriv et program som ber brukeren skrive inn to setninger. Programmet
#skal deretter sammenligne lengden på de to setningene og skrive ut hvilken
#som er lengst og antall karakterer det er i denne setningen.
#


# NEW
print("Setnignsjekk: lengst og antall karakterer.")
sentence1 = input("Skriv første setning.")
sentence2 = input("Skriv andre setning.")

#check length of both sentences and print the longest one with its length and character count, or if same length.
if len(sentence1) > len(sentence2):
    print (f"Dette er en den lengste av disse to setningene: {sentence1}. Den har {len(sentence1)} karakterer")
elif len(sentence1) == len(sentence2):
    print(f"Disse setningene er like lange. Dem har {len(sentence1)} karakterer.")
else:
    print (f"Dette er en den lengste av disse to setningene: {sentence2}. Den har {len(sentence2)} karakterer")




# ___________________________________________
# OLD CODE FROM TRY 1:
# sentence1 = input("Enter first of two sentences.")
# sentence2 = input("Enter second of two sentences.")
#check length of both sentences and print the longest one with its length and character count.
# if len(sentence1) > len(sentence2):
#  print (f"Dette er en den lengste av disse to setningene: {sentence1}. Den har {len(sentence1)} karakterer")
# else:
#  print (f"Dette er en den lengste av disse to setningene: {sentence2}. Den har {len(sentence2)} karakterer")
# ___________________________________________
