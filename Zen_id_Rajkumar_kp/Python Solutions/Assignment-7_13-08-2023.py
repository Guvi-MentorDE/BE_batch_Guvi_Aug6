#QUESTION:
#1. Create a base class called high_school
#    1.a) define a method , and define a static variable of pass mark = 40 
#2. create a child class caleed students 
#3. accept input list of marks for english, maths, science, social from studetns = [50,40,30,90] 
#4. inherit base class from child class
#5. determine if a student is pass of failed in respective subject

class high_school:
    pass_mark = 40 #static variable
class students(high_school):
    subjects = ["English","Maths","Science","Social"]
    marks = [int(item) for item in input().split()]  #get input from user as 50 40 30 90
    for item in range(len(marks)):
        if marks[item] >= high_school.pass_mark:
            print("Student passed in " + subjects[item])
        else:
            print("Student failed in " + subjects[item])

if __name__ == "__main__":
    s1 = students()