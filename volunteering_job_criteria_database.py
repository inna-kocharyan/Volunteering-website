Volunteering_Opportunity_1 = {
  "minimum age" : 18,
  "maximum age" : 20,
  "experience" : 3,
  "excel" : "yes",
  "English" : "beginner",
  "Russian" : "beginner"
}
Volunteering_Opportunity_2 = {
  "minimum age" : 16,
  "maximum age" : 19,
  "experience" : 1,
  "excel" : "no",
  "English" : "beginner",
  "Russian" : "intermediate"
}
Person1 = {
  "age" : input("Please incert your age\n"),
  "experience" : input("Please specify your experience in years\n"),
  "excel" : input("Can you use excel?\n"),
  "English" : input ("Please specify your level of English\n"),
  "Russian" : input("Please specify your level of Russian\n")
}
if (int(Volunteering_Opportunity_1["minimum age"]) <= int(Person1["age"]) <= int(Volunteering_Opportunity_1["maximum age"])):
  if (int(Person1["experience"]) >= int(Volunteering_Opportunity_1["experience"])):
   if (Person1["excel"] == Volunteering_Opportunity_1["excel"]):
     if (Person1["English"] == Volunteering_Opportunity_1 ["English"]):
       if (Person1["Russian"] == Volunteering_Opportunity_1["Russian"]):
         print("Volunteering Opportunity 1 Matches you")
else:
  if(int(Volunteering_Opportunity_2["minimum age"]) <= int(Person1["age"]) <= int(Volunteering_Opportunity_2["maximum age"])):
    if (int(Person1["experience"]) >= int(Volunteering_Opportunity_2["experience"])):
      if (Person1["excel"] == Volunteering_Opportunity_2["excel"]):
        if (Person1["English"] == Volunteering_Opportunity_2 ["English"]):
          if (Person1["Russian"] == Volunteering_Opportunity_2["Russian"]):
            print ("Volunteering Opportunity 2 Matches you")
            
