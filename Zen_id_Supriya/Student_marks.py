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

    def view_list_of_marks(self,lst_of_subjects,lst_of_marks):
        for i in range(0,len(lst_of_marks)):
            for j in range(0,len(lst_of_subjects)):
                if i==j:
                    #print("The list of subjects and their marks are:")
                    print(f"{lst_of_subjects[j]}:{lst_of_marks[i]}")
                #return lst_of_subjects[j],lst_of_marks[i]
    
                    

class students(high_school):
        
        def pass_or_fail(self,lst_of_subjects,lst_of_marks):
            for i in range(0,len(lst_of_marks)):
                for j in range(0,len(lst_of_subjects)):
                    if lst_of_marks[i]<40:
                        print(f"Student has failed in {lst_of_subjects[i]}")
                        break
                    else:
                        print(f"Student has passed in {lst_of_subjects[i]}")
                        break
            

if __name__ == "__main__":

    lst_subjects=["English","Maths","Science","Social"]
    lst_marks=[]
    stud=students(lst_subjects,lst_marks)
    for i in lst_subjects:
        lst_marks.append(int(input(f"Enter the mark for {i}: ")))
    print("Marks for subjects are:")
    stud.view_list_of_marks(lst_subjects,lst_marks)
    stud.pass_or_fail(lst_subjects,lst_marks)






    

