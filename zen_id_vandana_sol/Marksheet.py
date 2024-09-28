""" 
2. Create a base class called high_school
    1.a) define a method and define a static variable of pass mark = 40
2. Create a child class called students
3. accept input list of marks for english, maths, science, social from students = [50, 40, 30, 90]
4. inherit base class from child class
5. determine if a student is pass or failed in respective subject
"""
class high_school:
    passing_marks=40
    class students:
        def marksheet(self):
            self.marks={}
            Sub=["Maths","Science","Social science","English"]
            for i in Sub:
                print("enter marks of",i)
                self.marks[i]=int(input())
            return self.marks

        
        

         
                             


            
            
        

