class high_school:
    pass_mark =  40 #static variable
    def __init__(self,english,maths,science,tamil,social):
        self.english  = english
        self.maths    = maths
        self.science  = science
        self.tamil    = tamil
        self.social   = social
    def student(self):

       if (self.social < 40 or self.science < 40 or self.maths < 40
           or self.tamil < 40 or self.social < 40):
           return "fail"
       else:
           return "pass"

class display(high_school):
    def display_result(self):
          result = display.student(self)
          if result == "pass":
              print('You result is :',result)
          else:
              print('Your Result is:',result)


if __name__ == "__main__":
    en = int(input('Please enter the english mark:'))
    ma = int(input('Please enter the Maths Mark:'))
    ta = int(input('Please enter the tamil mark:'))
    sc = int(input('Please enter the science mark:'))
    soci = int(input('Please enter the social mark:'))

    schol = display(en,ma,sc,ta,soci)
    schol.display_result()
