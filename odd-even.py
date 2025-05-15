number = int(input("Enter a number between 1 and 100: "))

if number < 1 or number > 100:
    print("Number out of range.")
elif number % 2 == 0:
    print("The number is Even.")
else:
    print("The number is Odd.")

