#to check the age that the company wants#
age_min = int(input("Please enter the minimum age requered for this job\n"))
if age_min <= 15: 
    print(" this is under the state age limit")
else:
    print("")
age_max = int(input("Please enter the maximum age requered for this job\n"))
if age_max >= 60: 
    print(" Not possible")
else:
    print("")
    #this part has  word limit  for describing the company#

while True:
    answer = input("Please describe the job opportunity in 100 words\n")
    if len(answer) <= 100:
        break
    else:
        print("Too much info - keep it shorter!")
while True:
	try:
		number = int(input("what's the minimum years of work expiriance  that is required\n "))
		assert(number > 0), 'Number must be bigger than 0'
		break
	except:
		print("error")
		#this part is choosing languages and levels of the language#

choices = ['Native', 'intermediate', 'beginner ', 'not requiered']

language_level = {
  "English" : "",
  "German" : "",
  "Armenian" : ""

}

for key in language_level.keys():
  level = input("what is your level of " + key + ". Please select from the following choices: " + str(choices))

  if (level in choices):
    print("valid choice")
  else:
    print("invalid")

  language_level[key] = level

print(language_level)

#this is the last part after the whole coad is writen#
input(" please insert any website links (*not requiered*)\n")

#when dose the opertunity start and end##
import datetime
inputDate = input("Enter the date in format 'dd/mm/yy' : ")
day,month,year = inputDate.split('/')
isValidDate = True
try :
    datetime.datetime(int(year),int(month),int(day))
except ValueError :
    isValidDate = False
if(isValidDate) :
    print ("Input date is valid ..")
else :
    print ("Input date is not valid..")
#if interwiew is requered #
interview = (input("is an interwivew requiered? (y/n)\n"))
if interview=='No'or 'Yes' or 'no' or 'yes' :
    print("")
else:
    print("please enter a valid answere")
        #ask the location #
input("where is the job opertunity going to be held\n")