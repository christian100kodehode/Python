# Oppgave 5.4
# Lag en funksjon som lister opp alle bøkene som ikke ble levert tilbake.
# Returner en liste med navnene på bøkene og hvem som lånte dem og skriv
# ut svaret.

import csv
from datetime import datetime
import os

#Make a boolian True if ja
def parsed_bool(input_str: str) -> bool:
    return input_str.lower() == "ja"


def parse_csv_loans(filename: str) -> list[dict]:

    not_returned = []

    # Error checking and printing lines with error    
    errors = []


    #Check if file exists
    if not os.path.isfile(filename):
        print(f"Error: File \"{filename}\" does not exist.")
        return

    try:
        with open(filename, mode="r", encoding="utf-8") as f:
            reader = csv.reader(f)
            header = next(reader)  # Read header
            if len(header) != 8:
                print(f"Error: Invalid header. Expected 8 fields, got {len(header)}.")
                return
             
            # start iterating through the file
            for index, row in enumerate(reader, start=2):
                
                #Validate field count
                if len(row) != 8:
                    errors.append(f"Error in line {index}: Incorrect number of fields ({len(row)}). Expected 8. Line content: {",".join(row)}")
                    continue

                try:
                    #Unpack all fields for future use
                    first_name, last_name, book_title, category, loan_date, loan_days, extended_days, returned = [item.strip() for item in row]

                    # Validate non-empty strings
                    if not first_name or not last_name or not book_title or not category:
                        errors.append(f"Error in line {index}: Empty string in FirstName, LastName, BookTitle, or Category. Line content: {",".join(row)}")
                        continue

                    #Validate date
                    try:
                        datetime.strptime(loan_date, "%d/%m/%Y")
                    except ValueError:
                        errors.append(f"Error in line {index}: Invalid LoanDate format. Expected DD/MM/YYYY. Got: {loan_date}. Line content: {",".join(row)}")
                        continue

                    #Validate loan days
                    try:
                        loan_days = int(loan_days)
                        if loan_days < 0:
                            errors.append(f"Error in line {index}: LoanAmountofDays must be non-negative. Got: {loan_days}. Line content: {",".join(row)}")
                            continue
                    except ValueError:
                        errors.append(f"Error in line {index}: LoanAmountofDays must be integers. Got: {loan_days}. Line content: {",".join(row)}")
                        continue

                    #Validate extended
                    try:
                        
                        extended_days = int(extended_days)
                        if extended_days < 0:
                            errors.append(f"Error in line {index}: ExtendedLoan must be non-negative. Got: {extended_days}. Line content: {",".join(row)}")
                            continue
                    except ValueError:
                        errors.append(f"Error in line {index}: ExtendedLoan must be integers. Got: {extended_days}. Line content: {",".join(row)}")
                        continue

                    #Validate boolean returned if correct or not
                    if returned.lower() not in ("ja", "nei"):
                        errors.append(f"Error in line {index}: {e}. Line content: {",".join(row)}")
                        continue
                    
                    #Add lines to list that have false in the boolean check ("nei")
                    if not parsed_bool(returned):
                        not_returned.append(f"{first_name} {last_name}: {book_title}.")

                except Exception as e:
                    errors.append(f"Unexpected error in line {index}: {e}. Line content: {",".join(row)}")



    except Exception as e:
        print(f"Error reading file: {e}")
        return

    if errors:
        print(f"\nProcessed with {len(errors)} error(s):")
        for error in errors:
            print(error)

    return  not_returned



if __name__ == "__main__":
    filename = "bokutlån.csv"
    #unpack functions
    not_returned = parse_csv_loans(filename)
    print("\nBooks not returned:")
    for entry in not_returned:
        print(entry)

