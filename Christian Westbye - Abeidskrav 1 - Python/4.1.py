# 4 Opprette filstruktur og sortere filer
# Oppgave 4.1
# Lag en funksjon som oppretter en mappe kalt Files og genererer 30 tilfeldige
# filer med følgende filtyper i denne mappen: .txt, .csv, og .log. Hver fil
# skal ha:
# • Et tilfeldig navn med mellom 5 og 10 tegn.
# • En tilfeldig filtype valgt fra de tre typene.
# • Innhold i disse filen er ikke viktig — lag gjerne disse filene uten innhold
# Files
# | - - G5zLehz4 . txt
# | - - iTwTrTkU . txt
# | - - vPcaO7jR . csv
# | - - 1 Vgi2jbe . log
# ‘-- 7 NMaq7aa . csv
# 0 directories , 5 files

import os
import random
import string

def create_folder_and_files(folder_name, number_files, extensions, file_size=0):

    try:
        # Create the folder if it doesn"t exist
        os.makedirs(folder_name, exist_ok=True)
        print(f"Created folder: {folder_name}")

        # Generate random files
        for _ in range(number_files):
            # Create a random files with length between 5 and 10
            file_name = "".join(random.choices(string.ascii_lowercase + string.digits, k=random.randrange(5,10)))
            # Randomly select an extension
            extension = random.choice(extensions)
            # Combine folder path, file name, and extension
            file_path = os.path.join(folder_name, f"{file_name}{extension}")
            
            # Create the file
            with open(file_path, "wb") as f:
                if file_size > 0:
                    f.write(os.urandom(file_size))
            print(f"Created file: {file_path}")

        return True

    except Exception as e:
        print(f"Error: {e}")
        return False

# File and folder settings
folder_name = "Files"  # Name of the new folder
number_files = 30  # Number of files to create
extensions = [".txt", ".log", ".csv"]  # List of extensions
file_size = 0  # File size

# Create files
success = create_folder_and_files(folder_name, number_files, extensions, file_size)
if success:
    print("Operation completed successfully!")
else:
    print("Operation failed.")
