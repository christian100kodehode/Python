#3 Funksjoner
#Oppgave 3.1
#Lag en funksjon som tar inn en streng og sjekker om det er en gyldig
#IPv4-adresse. En gyldig IPv4-adresse har fire deler atskilt med punktum
#(_), der hver del er et heltall mellom 0 og 255. Funksjonen skal returnere
#True hvis det er en gyldig adresse, og False ellers. Eksempel:
#Input: "192.168.0.1" → Output: True
#Input: "256.100.50.0" → Output: False


# NEW

def check_valid_ipv4ip(ip):
    # seperate by "."
    segment= ip.split(".")
    #  if not 4 parts False
    if len(segment) != 4:
        return False
    # loop through all and check for empty segment
    for s in segment:
        if not s:
            return False
        #  value between 0 - 255 and no leading zeros - check done by comparing converted integer with original string, if not integer - safely exit with ValueError
        try:
            n = int(s)
            if n < 0 or n > 255 or s != str(n):
                return False
        except ValueError:
            return False
    return True


# test data
ip = "255.255.255.0"

print(f"Check if {ip} is valid? {check_valid_ipv4ip(ip)}")



# Variant using imports, here we use the built in ipadress import
# import ipaddress

# def check_ipv4_adress(ipv4_numbers: str):
#     try:
#         ipaddress.IPv4Address(ipv4_numbers)
#         print("True")
#     except ValueError:
#         print("False")


# print(f"'192.168.0.1' check ipv4 {check_ipv4_adress('192.168.0.1')}\n")
# print(f"'266.168.0.1' check ipv4 {check_ipv4_adress('266.168.0.1')}\n")




# ___________________________________________
# OLD CODE FROM TRY 1:

# def check_if_ip_is_valid(ip_adress_str):
    #split the ip by .

    # segments = ip_adress_str.split(".")
    #if not 4 different parts return False

    # if len(segments) != 4:
    #     return False
    #if one is empty return False

    # for segment in segments:
    #     if not segment:
    #         return False
        #check for leading 0, not allowing 01 and so on.

        # if len(segment) > 1 and segment[0] == "0":
        #     return False
        # if segment[0] == 0:
        #     return False
        #check if only digits

        # if not segment.isdigit():
        #     return False
        #check values are 

    #     num = int(segment)
    #     if not (0<= num <= 255):
    #         return False
    
    # return True


# Setup for using the function:

# ip = "0.1.5.2"
# result = check_if_ip_is_valid(ip)

# print(f"Check if {ip} is valid? {result}")

# ___________________________________________