Person1 = {
"age" : input("Please incert your age\n"),
"experience" : input("Please specify your experience in years\n"),
"excel" : input("Can you use excel?\n"),
"English" : input ("Please specify your level of English\n"),
"Russian" : input("Please specify your level of Russian\n")}
student_success_index = 0
opportunities = 4
count = 0
import csv
with open('opportunities.csv', 'r') as csv_file:
 csv_reader = csv.reader(csv_file)
 for line in csv_reader:
   if line[1] == Person1["age"]:
     student_success_index += 1
   if line[3] <= Person1["experience"]:
     student_success_index += 1
   if line [4] == Person1["excel"]:
     student_success_index += 1
   if line[5] == Person1["English"]:
     student_success_index += 1
   if line[6] == Person1["Russian"]:
     student_success_index += 1
 while count < opportunities and int(student_success_index) >= int(line[7]):
    print(line[0]) 
    count += 1 
    
         




