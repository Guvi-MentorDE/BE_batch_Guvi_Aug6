import math
class High_school:
    def get_pass_mark(self):
        self.pass_mark=40
        self.subjects=["English","Maths","Science","Social"]
    
class Students(High_school):
    def __init__(self,list_mark):
        self.list_mark=list_mark
    
    def check_pass_fail(self):
        count=0
        for i in self.list_mark:
            if(i<self.pass_mark):
                print("The student failed in",self.subjects[count])
            else:
                print("The student passed in",self.subjects[count])
            count=count+1

if __name__=="__main__":
    print("Enter the marks of the student in the order of English, Maths, Science and Social seperated by comma")
    mark_list=list(map(int,input().split(',')))
    student_object=Students(mark_list)
    student_object.get_pass_mark()
    student_object.check_pass_fail()











