#Oppgave 1.5
#U6
#| 1 | 2 | 3 |
#| - - -| - - -| - - -|
#| 1 | 2 | 3 |
#| 2 | 4 | 6 |
#| 3 | 6 | 9 |



# ----------------------- NEW - Change layout of table

while True:
    try:
        user_input_number = int(input("Enter number to multiply:"))
        user_input_start = int(input("Enter number to start from."))
        user_input_stop = int(input("Enter number to stop at."))
        block_to_use = "---"
        if user_input_start > user_input_stop:
            print("Select a valid range between start and stop.")
            continue
        #^5 specifies the total width of the padded output. ^ is center.
        print(f" |{user_input_number:^3}|{user_input_start:^3}|{user_input_stop:^3}|")
        print(f" |{block_to_use:^3}|{block_to_use:^3}|{block_to_use:^3}|")
        #start looping through the inputted numbers
        for i in range(user_input_start, user_input_stop + 1):
            result = user_input_number * i
            print(f" |{user_input_number:^3}|{i:^3}|{result:^3}|")
    except ValueError:
        print("Try again, only numbers allowed.")
    else:
        break

print(f"\nThe multiplication for {user_input_number}. Starting at {user_input_start } and stopping at {user_input_stop}.\n")

# ___________________________________________
# OLD CODE FROM TRY 1:

# while True:
#     try:
#         user_input_number = int(input("Enter number to multiply:"))
#         user_input_start = int(input("Enter number to start from."))
#         user_input_stop = int(input("Enter number to stop at."))
#         block_to_use = "-----"
#         if user_input_start > user_input_stop:
#             print("Select a valid range between start and stop.")
#             continue

        #^5 specifies the total width of the padded output. ^ is center.

        # print(f" |  {user_input_number:^5}  |  {user_input_start:^5}  |  {user_input_stop:^5}  |")
        # print(f" |  {block_to_use:^5}  |  {block_to_use:^5}  |  {block_to_use:^5}  |")

        #start looping through the inputted numbers

#         for i in range(user_input_start, user_input_stop + 1):
#             result = user_input_number * i
#             print(f" |  {user_input_number:^5}  |  {i:^5}  |  {result:^5}  |")
#     except ValueError:
#         print("Try again, only numbers allowed.")
#     else:
#         break

# print(f"\nThe multiplication for {user_input_number}. Starting at {user_input_start } and stopping at {user_input_stop}.\n")
# ___________________________________________