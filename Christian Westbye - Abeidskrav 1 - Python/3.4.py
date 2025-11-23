# Oppgave 3.4
# Lag en funksjon som tar en annen funksjon som parameter, noen argumenter
# og et forventet resultat, og som returnerer sant hvis det faktiske resultatet
# stemmer overens med det forventede resultatet, ellers usant.

# Check if a leap year with a function and a true/false message:
def is_leap_year(year):
    # Check the year:
    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)

def function_check_date(func, date_str):
    try:
        # Split the date entries by "/"
        day, month, year = map(int, date_str.split("/"))
        
        # Date check
        if not (1 <= month <= 12 and 1 <= day <= 31 and year > 0):
            return False
        
        # Apply the provided function to the year
        return func(year)
    # If not correct date, return False
    except ValueError:
        return False

# Test case:
date = "21/11/2025"
result = function_check_date(is_leap_year, date)
print(f"Is the year in {date} a leap year? {result}")