'''
Q1) 
1. Create a base class called high_school
    1.a) define a method and define a static variable of pass mark = 40
2. Create a child class called students
3. accept input list of marks for english, maths, science, social from students = [50, 40, 30, 90]
4. inherit base class from child class
5. determine if a student is pass or failed in respective subject
'''

#import, class (methods, instance variables), main, object


class high_school:
  pass_mark = 40
  def pass_fail(self, subjects, marks):
    a = []
    for s in range(len(self.subjects)):
      for m in range(len(self.marks)):
        if(s==m):
          if(self.marks[m]>=40):
            a.append(True)
            print(f"Passed in {self.subjects[s]} with {self.marks[m]}")
          else:
            a.append(False)
            print(f"Failed in {self.subjects[s]} with {self.marks[m]}")
    if(False in a):
      return("Result: Failed")
    else:
      return("Result: Passed")

class students(high_school):
  def __init__(self, subjects, marks):
    self.subjects = subjects
    self.marks = marks

  def marks_view(self, subjects, marks):
    print("Marks")
    for sub in range(len(self.subjects)):
      for mark in range(len(self.marks)):
        if(sub==mark):
          yield(f'{self.subjects[sub]}: {self.marks[mark]}')
  
  def is_valid_marks(self, marks):
    check_marks = [False for i in self.marks if(i>100)]
    return False if False in check_marks else True



if __name__ == '__main__':
  try:
    subjects = ["English", "Maths", "Science", "Social"]
    marks = []
    for i in subjects:
      marks.append(float(input(f"Enter the mark for {i}: ")))
    stud1 = students(subjects, marks)
    if(stud1.is_valid_marks(marks)):
      print("------------------View marksheet------------------")
      for i in stud1.marks_view(subjects, marks):
        print(i)
      print("------------------Evaluation------------------")
      print(stud1.pass_fail(subjects, marks))
    else:
      print("Enter valid marks")
  except ValueError as ve:
    print("Enter a decimal number: ", ve)
  except Exception as e:
    print("An exception was raised: ",e)
  finally:
    print("Thank you!")