# Ask the user for their age
age = int(input("Enter your age: "))

# Categorize based on the age
if age < 18:
    print("You are a minor.")
elif 18 <= age <= 65:
    print("You are an adult.")
elif age > 65:
    print("You are a senior.")
else:
    print("Invalid age entered.")
