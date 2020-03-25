Person1 = {
"age" : input("Please incert your age\n"),
"experience" : input("Please specify your experience in years\n"),
"excel" : input("Can you use excel?\n"),
"English" : input ("Please specify your level of English\n"),
"Russian" : input("Please specify your level of Russian\n")}

import csv
opp_list = ["Volunteering_Opportunity", "age", "experienc", "excel", "English", "Russian"]

with open ("opportunities.csv") as csvfile:
  reader = csv.DictReader(csvfile)
  for opp in reader:
    if int(opp["age"]) <= int(Person1["age"]) and int(opp["experience"]) <= int(Person1["experience"]) and opp["English"] == Person1["English"] and opp["Russian"] == Person1["Russian"]:
      print ("Congrats you match to the volunteering opportunity", opp["Volunteering_Opportunity"])
