required_age_min = 18
required_age_max = 20
exp = 3
vol_age = input("Please insert your age\n")

if(int(vol_age) < 18 or int(vol_age) > 20):
  print("Sorry. Your age does not match our criteria.")
else:
  vol_exp = int(input("Please enter your experience in this field"))
  if(vol_exp < exp):
    print("Sorry. You are not experienced enough.")
  else: 
    excel = str(input("do you know excel?\n"))
    russian = str(input("do you know Russian?\n"))
    english = str(input("do you know English?\n"))
    student_success_index = 2
    student_success_index1 = 0
    sum = 0
    if str(excel) == "yes":
      sum = sum + student_success_index1 + 1

    if str(russian) == "yes":
      sum = sum + student_success_index1 + 1

    if str(english) == "yes":
      sum = sum + student_success_index1 + 1

    if sum >= student_success_index:
      print("Success! You are invited to interview")
    else:
      print("Get over yourself")
