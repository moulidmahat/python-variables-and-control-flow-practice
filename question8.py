# Ask the user to enter a number (1 to 7)
day_number = int(input("Enter a number (1 to 7) representing the day of the week: "))

# Determine and print the corresponding day
if day_number == 1:
    print("Monday")
elif day_number == 2:
    print("Tuesday")
elif day_number == 3:
    print("Wednesday")
elif day_number == 4:
    print("Thursday")
elif day_number == 5:
    print("Friday")
elif day_number == 6:
    print("Saturday")
elif day_number == 7:
    print("Sunday")
else:
    print("Invalid input. Please enter a number between 1 and 7.")
