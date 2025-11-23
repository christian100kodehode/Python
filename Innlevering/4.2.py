# Oppgave 4.2
# Lag en funksjon som leser filene i Files og sorterer dem i undermapper
# basert på filtype:
# • Opprett en ny mappe kalt SortedFiles
# • Opprett undermapper kalt txt-files, csv-files, og log-files inne
# i denne mappen kalt SortedFiles.
# • Flytt filene fra Files til riktig undermappe i SortedFiles basert på
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




# select directory to work on
# target_directory = "./Files/"
# subfolder to keep all new folders inside
# subfolder = "SortedFiles"

# make list of files from target_directory
# files = [f for f in os.listdir(target_directory) if os.path.isfile(os.path.join(target_directory, f))]

# iterate through files and move to correct folder
# for filename in files:
#     name, extension = os.path.splitext(filename)
#     if extension:
#         destination_folder = os.path.join(target_directory, subfolder, extension)

#         if not os.path.exists(destination_folder):
#             os.makedirs(destination_folder)

#         source_path=os.path.join(target_directory, filename)
#         destination_path = os.path.join(destination_folder, filename)
#         shutil.move(source_path, destination_path)

# NEW
# using shutil for file operations, pathlib for paths handling, 
import shutil
from pathlib import Path
from typing import List


# Start function: move files in target_dir (string or Path) into subfolder (string), by their extension into SortedFiles folder, return True if success.
def move_by_extension(target_dir: str | Path, subfolder: str = "SortedFiles") -> bool:

    # make path absolute in filesystem
    target_dir = Path(target_dir).resolve()
    # check if target is a valid folder
    if not target_dir.is_dir():
        return False
    
    # make list of all files using pathlib folder object target_dir iterdir loops through each entry
    files: List[Path] = [f for f in target_dir.iterdir() if f.is_file()]
    if not files:
        return False
            
    # create the path to use, exist_ok avoid error if exists
    sorted_root = target_dir/subfolder
    sorted_root.mkdir(exist_ok=True)

    # loop through each file in the list, get extension without the "." Skip of no extension
    for file_path in files:
        suffix = file_path.suffix.lstrip(".")
        if not suffix:
            continue
    
        # make folders for the files and set destination path for file
        dest_folder = sorted_root/suffix
        dest_folder.mkdir(exist_ok=True)
        dest_path = dest_folder/file_path.name

        # move file
        try:
            shutil.move(str(file_path), str(dest_path))
            print(f"Moved {file_path.name} to /{dest_folder.name}/")
        except Exception as e:
            print(f"Failed to move {file_path.name}: {e}")

    return True

#  Print victory or loss
success = move_by_extension("./Files", "SortedFiles")
if success:
    print(f"Finished moving files.")
else:
    print("Failed moving files.")
