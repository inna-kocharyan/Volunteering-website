language_levels = {
  "native" : 4,
 "advanced" : 3,
 "intermediate" : 2,
 "beginner" : 1,
 "not_required" : 0}

age = int(input("Please enter your required minimum age"))

Russian = int(input("Please enter your required level of Russian from scale of 0 to 4. Level criteria are following: " + str(language_levels)))
if Russian <=4:
  print("Thank you")
else:
  print("Please type an integer from 0 to 4")

English = int(input("Please enter your required level of English from scale of 0 to 4."))
if English <=4:
  print("Thank you")
else:
  print("Please type an integer from 0 to 4")

Armenian = int(input("Please enter your required level of Armenian from scale of 0 to 4."))
if Armenian <=4:
  print("Thank you")
else:
  print("Please type an integer from 0 to 4")

German = int(input("Please enter your required level of German from scale of 0 to 4."))
if German <=4:
  print("Thank you")
else:
  print("Please type an integer from 0 to 4")

import csv
col_list = ["First Name", "Last Name", "Age", "English", "Armenian", "German", "Russian"]

with open ("Volunteer_matching.csv") as csvfile:
  reader = csv.DictReader(csvfile)
  for col in reader:
    if (int(col["Age"]) >= age   and int(col["Russian"]) >= Russian and int(col["English"])>= English and int(col["Armenian"])>= Armenian and int(col["German"]) >= German):
      print (col["First Name"], col["Last Name"]) 
    
      

