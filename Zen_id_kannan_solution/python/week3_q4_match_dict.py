"""
  Assignment : Week 3 - Q4 - Get matching keys
  Author  :   Kannan Kandasamy
  Course  :   ML Guvi - Python
  Date    :   15/08/2023
  Details :   Get an input of two dictionaries and output matching key and value
"""

class Dictionaries:
  def __init__(self,s1="",s2=""):
    self.str1 = s1
    self.str2 = s2

  def get_matching(self,d1={},d2={}):
    m_keys = set(d1.keys()) & set(d2.keys())
    m_op = {i:d1[i] for i in m_keys}
    return m_op

#main function
if __name__ == "__main__":
  n1 = int(input("Enter first dictionary size : "))
  ip1 = {input("key:"):input("value:") for i in range(n1)}
  n2 = int(input("Enter first dictionary size : "))
  ip2 = {input("key:"):input("value:") for i in range(n2)}  
  #d1 = {"INDIA": "INR", "US": "USD"}
  #d2 = {"INDIA": "INR", "UK": "GBP", "JAPAN": "YEN"}
  obj = Dictionaries()
  op = obj.get_matching(ip1, ip2)
  print(op)