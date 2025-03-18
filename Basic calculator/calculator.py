userinput=input("Use an operator:: +,-,/,*: ")

num1=float(input("Enter the first number"))

num2=float(input("Enter the second number"))


if userinput=="+":
  print(f"Sum of the number is: {round(num1+num2,2)}")
elif userinput =="-":
  print(f"sub of the number is:{round(num1-num2,2)} ")
elif userinput=="/":
  print(f"divison of the number is: {round(num1/num2)}")
elif userinput == "*":
  print(f"multiplay of the number is: {round(num1*num2)}")
else:
  print("Enter a valid opreator")
