#import
pass_mark = 40

class high_school:
    def student_passmark(self):
        print(f"The pass mark for all subjects is {pass_mark}\n")

class students(high_school):
    def __init__(self, name, subject, marks):
        self.name = name
        self.subject = subject
        self.marks = marks

    def student_pass_or_fail (self):
        if self.marks >= pass_mark:
            print(f"{self.name} has passed {self.subject} with {self.marks} marks\n")
        else:
            print(f"{self.name} has failed {self.subject} with {self.marks} marks\n")

if __name__ == "__main__":
    print("Enter student name :\n")
    stud_name = input()

    print("Enter the list of marks for maths, english, science respectively...\n")
    mark_inp = input()
    list_of_marks = mark_inp.split(',')

    listofsubjects = ['maths', 'english', 'science']

    main_obj = students(stud_name, None, None)
    main_obj.student_passmark()

    del main_obj

    for i, subjects in enumerate(listofsubjects):
        
        main_obj = students(stud_name, subjects, int(list_of_marks[i]))

        main_obj.student_pass_or_fail()
