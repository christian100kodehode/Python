#Oppgave 3.2
#Lag en funksjon som tar inn to datoer som strenger på formatet “dd/mm/yyyy”
#og returnerer antall dager mellom dem. Hvis den første datoen er senere enn
#den andre, skal funksjonen fortsatt returnere antall dager (positivt tall).
#Eksempel:
#Input: "21/11/2024", "01/01/2024" → Output: 325 dager

# find out if a leap year or not, leap year can be divided by 4, and not by 100 or 400
def is_leap_year(year):
    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)

#Find amount of days in each month
def days_in_month(year, month):
    if month == 2:
        return 29 if is_leap_year(year) else 28
    elif month in (4, 6, 9, 11):
        return 30
    else:
        return 31

#check total days
def total_days_from_reference(year, month, day):
    total_days = 0
    for y in range(1, year):
        total_days += 366 if is_leap_year(y) else 365
    for m in range(1, month):
        total_days += days_in_month(year, m)
    total_days += day
    return total_days

def days_between_dates(year1, month1, day1, year2, month2, day2):
    days1 = total_days_from_reference(year1, month1, day1)
    days2 = total_days_from_reference(year2, month2, day2)
    return abs(days2 - days1)

def is_valid_date(day, month, year):
    # Check if year is positive
    if year < 1:
        return False
    # Check if month is valid
    if not (1 <= month <= 12):
        return False
    # Check if day is valid for the given month and year
    max_days = days_in_month(year, month)
    if not (1 <= day <= max_days):
        return False
    return True

def parse_date(date_str):
    try:
        # Split the date string by "/"
        day, month, year = map(int, date_str.split("/"))
        return day, month, year
    except ValueError:
        return None  # Return None if invalid format or not a number

# Main program to accept user input
def main():
    # Prompt for two dates
    date1_str = input("Enter the first date (DD/MM/YYYY, e.g., 21/11/2020): ")
    date2_str = input("Enter the second date (DD/MM/YYYY, e.g., 15/01/2023): ")

    # Parse the dates
    date1 = parse_date(date1_str)
    date2 = parse_date(date2_str)

    # Check the parsing is valid
    if not date1 or not date2:
        print("Error: Invalid date format. Please use DD/MM/YYYY with valid numbers.")
        return

    day1, month1, year1 = date1
    day2, month2, year2 = date2

    # check if valid dates
    if not is_valid_date(day1, month1, year1):
        print(f"Error: {date1_str} is not a valid date.")
        return
    if not is_valid_date(day2, month2, year2):
        print(f"Error: {date2_str} is not a valid date.")
        return

    # Calculate days between dates
    days_diff = days_between_dates(year1, month1, day1, year2, month2, day2)
    print(f"Days between {date1_str} and {date2_str}: {days_diff}")

# Run the program
if __name__ == "__main__":
    main()

# Example using default import datetime
# from datetime import datetime

# def find_days_between(start_date: str, stop_date: str, date_format: str):
#     try:
#         print("Find out how many days untill specific date.\n")
#         start_date = datetime.strptime(start_date, date_format)
#         stop_date = datetime.strptime(stop_date , date_format)

#         days_between = start_date - stop_date
      
        
#         return abs(days_between).days
#     except ValueError:
#         print("Wrong format, please use DD/MM/YYYY.")
 

# date_start = "01/01/2025"
# date_stop = "01/10/2025"


# date_start2 = datetime.today().strftime("%d/%m/%Y")
# date_stop2 = "24/12/2025"
# date_format_example = "%d/%m/%Y"


# print(f"Days unil {date_stop2}:\n   {find_days_between(date_start2, date_stop2, date_format_example )} days.")      