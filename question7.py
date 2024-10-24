# Ask the user for the lengths of the three sides of the triangle
side1 = float(input("Enter the length of the first side: "))
side2 = float(input("Enter the length of the second side: "))
side3 = float(input("Enter the length of the third side: "))

# Determine the type of triangle
if side1 == side2 == side3:
    print("The triangle is equilateral (all sides are equal).")
elif side1 == side2 or side2 == side3 or side1 == side3:
    print("The triangle is isosceles (two sides are equal).")
else:
    print("The triangle is scalene (all sides are different).")
