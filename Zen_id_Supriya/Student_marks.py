# Q1) 
# 1. Create a base class called high_school
#     1.a) define a method and define a static variable of pass mark = 40
# 2. Create a child class called students
# 3. accept input list of marks for english, maths, science, social from students = [50, 40, 30, 90]
# 4. inherit base class from child class
# 5. determine if a student is pass or failed in respective subject

#import

pass_mark=40
class high_school:

    def __init__(self,lst_of_marks,lst_of_subjects):
        self.lst_of_subjects=lst_of_subjects
        self.lst_of_marks=lst_of_marks

    def view_list_of_marks(self):
        for i in range(0,len(self.lst_of_marks)):
            for j in range(0,len(self.lst_of_subjects)):
                if i==j:
                    print(f"{self.lst_of_subjects}:{self.lst_of_marks}")

class students(high_school):
        
        def pass_or_fail(self):
            for i in range(0,len(self.lst_of_marks)):
                for j in range(0,len(self.lst_of_subjects)):
                    if self.lst_of_marks[i]<40:
                        print(f"Student has failed in {self.lst_of_subjects[i]}")
                    else:
                        print(f"Student has passed in {self.lst_of_subjects[i]}")
                
                        return self.lst_of_subjects[i]

if __name__ == "__main__":

    lst_subjects=["English","Maths","Science","Social"]
    lst=[]
    stud=students(lst_subjects,lst)
    subjects=int(input("Enter no.of subject marks"))
    for i in range(0,subjects):
        marks=int(input())
        lst.append(marks)
   #stud.view_list_of_marks)
    
    stud.pass_or_fail()






    

