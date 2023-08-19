class High_school:
    pass_mark= 40

class Student(High_school):
    def __init__(self, marks):
        self.marks= marks
    def is_pass(self):
        result= []
        for _ in self.marks:
            if _ > High_school.pass_mark:
                result.append('pass')
            else:
                result.append('fail')
        return result
        

if __name__ == "__main__":
    x= Student([50,40,30,90])
    finalResult= x.is_pass()
    print(str(finalResult))