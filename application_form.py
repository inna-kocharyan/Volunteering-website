#application form for users (part 1) and collecting them (part 2)
#part 1
current_year = 2020
minimum_age = 14
maximum_age = 61
print("This is your application form please insert your data")
name = input("Please, enter your name : ") 
surname = input("Please, enter your surname : ")
year = input("Please, enter the year of your birth : ")

current_maximum_age = current_year - int(year)
print("Your age this year will be" + str(current_maximum_age) + ", so")

if current_maximum_age <= minimum_age:
  print ("Dear " + name + ", Sorry you are not acceptable forv any volunteering experience, yet.")
elif current_maximum_age >= maximum_age:
  print ("Dear " + name + ", You are already oldaged, please, #stayathome for your health")
else :
  print ("Dear " + name + ", You are in desired age group")

gender = int(input("Choose your gender 'number' \n1. female \n2. male \n answer : "))

while gender < 1 or gender > 2:
  print("Your input is not required number, please enter a proper one only".format(input=gender))
  gender = int(input("Choose your gender 'number' \n1. female \n2. male \nanswer")) 
else:
    print("Thanks")

if gender == 1:
  marriage = input("Are you married 'yes' or 'no' : ")
  position = " Ms. "
else:
  army_service = input("Have you served in army 'yes' or 'no' : ")
  position = "Mr."

listlanguages = []
number_of_languages = int(input("Dear " + name + ", how many languages do you know? "))
for i in range(number_of_languages): 
  number_of_languages = i + 1
  input_string = input("Enter your known language number " + str(int(i+1)) + " " )
  listlanguages.append(input_string)

  #PART2
print("THANK YOU")
print("Your data is stored" + position + " " + surname + " " + name)
print("Your maximum age this year is " + str(current_maximum_age))
print("Your known languages are ", listlanguages)
