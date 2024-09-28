'''
#Q1) 
1. Create a base class called high_school
    1.a) define a method , and define a static variable of pass mark = 40 
2. create a child class caleed students 
3. accept input list of marks for english, maths, science, social from studetns = [50,40,30,90] 
4. inherit base class from child class
5. determine if a student is pass of failed in respective subject 

#import , class (methods , instance variables) , main , object 
'''


class high_school:
    pass_mark = 40 
    
    def ispass(self,mark):
        if mark>=40 :
            return "Pass"
        else:
            return "Fail"


class students(high_school):
    def __init__(self,student,marklist):
        self.student=student
        self.marklist=marklist

    def report_card(self):
        report_dict = {

            "student_name":self.student,
            "English": self.ispass(self.marklist[0]),
            "Maths":self.ispass(self.marklist[1]),
            "Science":self.ispass(self.marklist[2]),
            "Social:":self.ispass(self.marklist[3]),

        } 
        return report_dict   

if __name__=="__main__":

    studentname=str(input("Enter Student Name:")) 
    marklist=list(map(int,input("Enter English,Maths,Science,Social marks in the same order: ").split(' ')))       
    print(marklist)
    student = students(studentname,marklist)

    print(student.report_card())