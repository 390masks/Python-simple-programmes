user=input("Create your user name").strip()

if len(user) > 12:
  print("user name should only contain less than 12 charaters")

elif not user.find(" ") ==-1:
  print("user name should not be contain spaces")

elif not user.isalpha():
  print("user name must only contain alphabets")
  
else:
  print(f"!Welcome {user}")
