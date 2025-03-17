unit = input("Enter your Temperature unit (C/F): ").strip().lower()
temp = float(input("Enter Temperature: "))

if unit == "c":
    temp = (9/5 * temp) + 32
    print(f"Converted Fahrenheit: {round(temp, 2)}°F")
elif unit == "f":
    temp = (temp - 32) / 1.8
    print(f"Converted Celsius: {round(temp, 2)}°C")
else:
    print(f"'{unit}' is not a valid temperature unit.")
