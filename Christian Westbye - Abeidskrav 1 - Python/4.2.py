# Oppgave 4.2
# Lag en funksjon som leser filene i Files og sorterer dem i undermapper
# basert p˚a filtype:
# • Opprett en ny mappe kalt SortedFiles
# • Opprett undermapper kalt txt-files, csv-files, og log-files inne
# i denne mappen kalt SortedFiles.
# • Flytt filene fra Files til riktig undermappe i SortedFiles basert p˚a
# deres filtype.
# SortedFiles
# | - - csv
# | | - - vPcaO7jR . csv
# | ‘-- 7 NMaq7aa . csv
# | - - log
# | ‘-- 1 Vgi2jbe . log
# ‘-- txt
# | - - G5zLehz4 . txt
# ‘-- iTwTrTkU . txt
# 3 directories , 5 files

import os
import shutil

# select directory to work on
target_directory = "./Files/"
# subfolder to keep all new folders inside
subfolder = "SortedFiles"

# make list of files from target_directory
files = [f for f in os.listdir(target_directory) if os.path.isfile(os.path.join(target_directory, f))]

# iterate through files and move to correct folder
for filename in files:
    name, extension = os.path.splitext(filename)
    if extension:
        destination_folder = os.path.join(target_directory, subfolder, extension)

        if not os.path.exists(destination_folder):
            os.makedirs(destination_folder)

        source_path=os.path.join(target_directory, filename)
        destination_path = os.path.join(destination_folder, filename)
        shutil.move(source_path, destination_path)