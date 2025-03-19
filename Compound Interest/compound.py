principle = 0
rate = 0
time = 0

while True:
  principle=float(input("Enter your principle amount: "))
  if principle < 0:
    print("Principle amount can't  be less than zero")
  else:
    break

while True:
  rate=float(input("Enter your rate of interst: "))
  if rate < 0:
    print("Rate of interst can't be less than zero")
  else:
    break
while True:
  time=float(input("Enter your time in years: "))
  if time < 0:
    print("Time cant be less than zero")
  else:
    break
total= principle * pow( 1 + rate / 100 ,time)

print (f"Total amount you have to pay for {principle}  for {time} years is: {total}")
