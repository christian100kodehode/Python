# 2.1 Test 

# Check valid date

#Find out if a leap year or not, leap year can be divided by 4, and not by 100 or 400
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

def is_valid_date(day, month, year):
    #Check if year is positive
    if year < 1:
        return False
    #Check if month is valid
    if not (1 <= month <= 12):
        return False
    #Check if day is valid for the given month and year
    max_days = days_in_month(year, month)
    if not (1 <= day <= max_days):
        return False
    return True

#parse date in correct way (DD/M/YYYY)
def parse_date(date_str):
    try:
        #Split the date string by "/"
        day, month, year = map(int, date_str.split("/"))
        return day, month, year
    except ValueError:
        return None  # Return None if invalid format or not a number

# Main program to accept user input
def main():
    #Prompt for date
    date1_str = input("Enter date (DD/MM/YYYY, e.g., 21/11/2020): ")
   

    # Parse the date
    date1 = parse_date(date1_str)
    

    # Check the parsing is valid
    if not date1:
        print("Error: Invalid date format. Please use DD/MM/YYYY with valid numbers.")
        return
    
    #unpack parsed date
    day1, month1, year1 = date1
    

    # check if valid dates
    if is_valid_date(day1, month1, year1):
        print(f"Error: {date1_str} is a valid date.")
    else:
        print(f"Error: {date1_str} is not a valid date.")

# Run the program
if __name__ == "__main__":
    main()