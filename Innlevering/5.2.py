# Oppgave 5.2
# Lag en funksjon som beregner hvor mange bøker som er lånt ut per sjanger
# (f.eks. "Fantasy: 3, Krim: 5", osv.) og skriv ut svaret.

import csv
from datetime import datetime
import os

#Make a booliean option based on ja/nei returned
def  parsed_bool(input_str: str) -> bool:
    if input_str.lower() in "ja":
        return True
    if input_str.lower() in "nei":
        return False

def parse_csv_loans(filename: str) -> list[dict]:
    category_counts = {}
    errors = []

    #Check if file exists
    if not os.path.isfile(filename):
        print(f"Error: File '{filename}' does not exist.")
        return category_counts

    try:
        with open(filename, mode='r', encoding='utf-8') as f:
            reader = csv.reader(f)
            header = next(reader)  # Read header
            if len(header) != 8:
                print(f"Error: Invalid header. Expected 8 fields, got {len(header)}.")
                return category_counts
            # start iterating through the 
            for index, row in enumerate(reader, start=2):
                
                #Validate field count
                if len(row) != 8:
                    errors.append(f"Error in line {index}: Incorrect number of fields ({len(row)}). Expected 8. Line content: {','.join(row)}")
                    continue

                try:
                    #Unpack all fields for future use
                    first_name, last_name, book_title, category, loan_date, loan_days, extended_days, returned = [item.strip() for item in row]

                    # Validate non-empty strings
                    if not first_name or not last_name or not book_title or not category:
                        errors.append(f"Error in line {index}: Empty string in FirstName, LastName, BookTitle, or Category. Line content: {','.join(row)}")
                        continue

                    #Validate date
                    try:
                        datetime.strptime(loan_date, '%d/%m/%Y')
                    except ValueError:
                        errors.append(f"Error in line {index}: Invalid LoanDate format. Expected DD/MM/YYYY. Got: {loan_date}. Line content: {','.join(row)}")
                        continue

                    #Validate loan days
                    try:
                        loan_days = int(loan_days)
                        if loan_days < 0:
                            errors.append(f"Error in line {index}: LoanAmountofDays must be non-negative. Got: {loan_days}. Line content: {','.join(row)}")
                            continue
                    except ValueError:
                        errors.append(f"Error in line {index}: LoanAmountofDays must be integers. Got: {loan_days}. Line content: {','.join(row)}")
                        continue

                    #Validate extended
                    try:
                        
                        extended_days = int(extended_days)
                        if extended_days < 0:
                            errors.append(f"Error in line {index}: ExtendedLoan must be non-negative. Got: {extended_days}. Line content: {','.join(row)}")
                            continue
                    except ValueError:
                        errors.append(f"Error in line {index}: ExtendedLoan must be integers. Got: {extended_days}. Line content: {','.join(row)}")
                        continue


                    #Validate boolean
                    try:
                        parsed_bool(returned)
                    except ValueError as e:
                        errors.append(f"Error in line {index}: {e}. Line content: {','.join(row)}")
                        continue

                    # Count category
                    category_counts[category] = category_counts.get(category, 0) + 1

                except Exception as e:
                    errors.append(f"Unexpected error in line {index}: {e}. Line content: {','.join(row)}")

    except Exception as e:
        print(f"Error reading file: {e}")
        return category_counts

    if errors:
        print(f"\nProcessed with {len(errors)} error(s):")
        for error in errors:
            print(error)

    return category_counts

if __name__ == '__main__':
    filename = 'bokutlån.csv'
    category_counts = parse_csv_loans(filename)
    print("\nCategory Counts:")
    for category, count in sorted(category_counts.items()):
        print(f"{category}: {count}")
