# Oppgave 5.3
# Beregn den gjennomsnittlige låneperioden i antall hele dager for alle bøker
# som er lånt ut, inkludert forlengelsene og skriv ut svaret.

import csv
from datetime import datetime
import os

# cout all lnes in csv
def count_lines(filepath):
    with open (filepath, "r") as file:
        return sum(1 for _ in file)
    
filepath = "bokutlån.csv"
total_lines = count_lines(filepath)


# Make a booliean based on ja/nei returned
def  parsed_bool(input_str: str) -> bool:
    if input_str.lower() in "ja":
        return True
    if input_str.lower() in "nei":
        return False

def parse_csv_loans(filename: str) -> list[dict]:
    errors = []
    total_days = 0
    all_extended = 0
    unvalid_rows = 0

    # check file excist or not
    if not os.path.isfile(filename):
        print(f"File {filename} do not excist")
        return

    try:
        with open (filename, mode="r", encoding="utf-8") as f:
            reader = csv.reader(f)
            # read header part, first line
            header = next(reader)
            # check if 8 parts
            if len(header) != 8:
                print(f"Error, wrong amopunt of parts in header, must be 8, now is {len(header)}.")
                return
            
            for index, row in enumerate(reader, start=2):
                # check if 8 parts here also
                if len(row) != 8:
                    errors.append(f"Error in line {index}, must be 8, check line has {len(row)} fields.")
                    continue
                
                try:
                    #Unpack fields
                    first_name, last_name, book_title, category, loan_date, loan_days, extended_days, returned = [item.strip() for item in row]
                    #Validate non-empty strings
                    if not first_name or not last_name or not book_title or not category:
                        errors.append(f"Error in line {index}: Empty string in FirstName, LastName, BookTitle, or Category. Line content: {','.join(row)}")
                        continue
                    

                    # check if date is valed
                    try:
                        datetime.strptime(loan_date, '%d/%m/%Y')
                    except ValueError:
                        errors.append(f"Error in line {index}: Invalid LoanDate format. Expected DD/MM/YYYY. Got: {loan_date}. Line content: {','.join(row)}")
                        continue

                    # check if loan days are a valid number and over 0
                    try:
                        loan_days = int(loan_days)
                        extended_days = int(extended_days)
                        if loan_days < 0 or extended_days < 0:
                            errors.append(f"Error in line {index}: LoanAmountofDays or ExtendedLoan must be non-negative. Got: {loan_days}, {extended_days}. Line content: {','.join(row)}")
                            continue
                    except ValueError:
                        errors.append(f"Error in line {index}: LoanAmountofDays or ExtendedLoan must be integers. Got: {loan_days}, {extended_days}. Line content: {','.join(row)}")
                        continue

                    # Validate boolean
                    try:
                        returned_bool = parsed_bool(returned)
                    except ValueError as e:
                        errors.append(f"Error in line {index}: {e}. Line content: {','.join(row)}")
                        continue

                    #Get total loan days
                    all_extended += extended_days
                    total_days += loan_days

                except Exception as e:
                    errors.append(f"Unexpected error in line {index}: {e}. Line content: {','.join(row)}")

    except Exception as e:
        print(f"Error reading file: {e}")
        return
    
    #Loop through errors
    if errors:
        print(f"\n{len(errors)} lines with errors, please correct:")
        for error in errors:
            print(error)
    
    #List unvalid rows
    unvalid_rows = len(errors)
    unvalid_rows = int(unvalid_rows)

    return  all_extended, total_days, unvalid_rows

if __name__ == '__main__':
    filename = 'bokutlån.csv'
    #unpack functions needed
    all_extended, total_days, unvalid_rows = parse_csv_loans(filename)
    days_borrowed_total = all_extended + total_days
    print("\nAverage length of loan:")
    total_average = days_borrowed_total / (total_lines - 1 - unvalid_rows)
    print(int(total_average))
