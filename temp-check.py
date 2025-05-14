temperature = float(input("Enter the temperature in °C: "))

if temperature > 30:
    print("It's hot outside!")
elif temperature >= 20:
    print("The weather is nice.")
elif temperature >= 10:
    print("It's a bit chilly.")
else:
    print("It's cold!")

