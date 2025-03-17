weight=input("Enter weight in kg or pound (k/p): ")
value=float(input("Enter your actual weight: "))

if weight=="p":
  value=value*0.453592
  print(f"Your weight converted into Kg is: {round(value,2)}kg")
elif weight =="k":
  value=value*2.2046
  print(f"Your weight converted into pounds is: {round(value,2)}lbs")
else:
  print(f"{weight} is not a unit of weight")
