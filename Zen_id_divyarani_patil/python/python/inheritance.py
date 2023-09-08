class highschool:
  pass_mark = 40
  def __init__(self):
    pass

class students(highschool):
  def check(self,marks):
    if(inp <= marks):
      print(" failed")
    else:
      print("pass")

if __name__=="__main__":
  inp = input("Enter science,social,english,maths marks : ")
  store = students()
  store.pass_mark
  store.check(inp)