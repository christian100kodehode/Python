#Oppgave 3.3
#I dataprogrammering brukes fargekoder ofte for˚a representere farger i brukergrensesnitt
#og grafikk. To vanlige måter å representere farger på er:
#1. Hex-kode: En fargekode som starter med # og består av seks tegn
#som representerer de røde, grønne og blå komponentene i fargen (for
#eksempel #CD5C5C). Hver komponent har to tegn (heksadesimalt),
#hvor:
#• CD representerer rødt (r),
#• 5C representerer rødt (g), og
#• 5C representerer blått (b),
#2. RGB-kode: En fargekode representert som tre heltall, ´en for hver
#fargekomponent (rød, grønn, bl˚a). For eksempel: rgb(205, 92, 92).
#
#Lag en funksjon rgb to hex som tar inn tre heltall (for eksempel red=205,
#green=92, blue=92) og returnerer tilsvarende Hex-kode som en streng (for
#eksempel "#CD5C5C"). Legg også til passende feilmelding om red, blue eller
#green parametere har ugyldig verdi.

def rgb_to_hex(r : int, g : int, b : int):        
    print(f"You entered values: {{'r': {r}, 'g': {g}, 'b': {b}}}.")
    #check if value is a whole number and not a string
    if not all(isinstance(n, int)for n in (r,g,b)):
        print("\nError. Please only use numbers.")
        return ""
    
    #make a empty list to store errors, and appent to the empty list if occurs
    errors = []
    if r < 0 or r >= 256:
        errors.append(f"Check value for r. You entered {r}.")
    if g < 0 or g >= 256:
        errors.append(f"Check value for g. You entered {g}.")
    if b < 0 or b >= 256:
        errors.append(f"Check value for b. You entered {b}.")
    if errors:
        for error in errors:
            print(f"{error}")
        print("\nError! RGB values must be be between 0 and 255")
        return ""
    else:
        return f"\nHex code is #{r:02X}{g:02X}{b:02X}"


#enter r g b numbers in the try to check:
try:
    print(rgb_to_hex(253, 3, 2))  # Valid input
except NameError as e:
    print(f"Error: {e}.")