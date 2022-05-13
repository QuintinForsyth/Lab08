count = 0
students = []
name = ""
grade = 0
student = []

def best_Student(students):
  """
  name of student with highest grade
  """
  win_Grade = 0
  win_Name = 0
  for student in students:
    grade = student[1]
    name = student[0]
    print(grade, name)
    if grade > win_Grade:
      win_Grade = grade
      win_Name = name
      
    elif win_Grade == grade:
      win_Name = win_Name +f", {name}"
    else:
      continue
  print(win_Name , win_Grade)
  return win_Name, win_Grade
    

def get_Avg (students):
  total = 0
  for student in students:
    total+= student[1]

  average = total / len(students)
  return average
  
def name_Ret (message):
  """
  gets name from the user based off of a message
  """
  while True:
    name = input(message)
    if (name == "exit" or name == "Exit" or name == "-1"):
      return "exit"
    return name
  

def num_Ret (message, name):
  
  """
  gets number from the user base off of a message
  """
  while True:
    try:
      grade = int(input(message))
      if (grade > 100 or grade < 0):
        print("invalid grade input, Grade cannot a exceed 100 or be less than 0")
        continue
      return grade
    except:
      print("You did not provide a number")
    
      
while name != "exit" or name != "Exit" or name != "-1":
  name = name_Ret("if name is -1 or Exit you will close the program and see the list you created else\nenter a name: ")
  if name == "exit":
    break
  grade = num_Ret(f"Enter {name.capitalize()}'s grade: ", name)
  student.append(name)
  student.append(grade)
  students.append(student)
  student = []
print(students)
average = get_Avg(students)
average = round(average,2)
print(f"The class average is: {average}")
best, best_grade = best_Student(students)
print(f"{best} {best_grade}")
if "," not in best:
  print(f"The Student with the highest grade is {best} with the grade of {best_grade}")
else:
  print(f"The Students with the highest grade are {best} they both had the grade of {best_grade}")