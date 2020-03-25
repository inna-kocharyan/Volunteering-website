choices = ["very bad", "bad", "ok", "good", "excellent"]

evaluation_criteria = {
  "responsibility" : "",
  "time-management" : "",
  "cooperation" : "",
  "language" : "",
  "organisational skills" : "",
  "project management" : ""}

for key in evaluation_criteria.keys():
  quality = input("What was the level of " + key + " of the volunteer?. Please choose from the following choices: " + str(choices) )
  
  if quality in choices:
    print("Thank you")
  else:
    print("Invalid. Please try again")
  
  evaluation_criteria[key] = quality

print(evaluation_criteria)
