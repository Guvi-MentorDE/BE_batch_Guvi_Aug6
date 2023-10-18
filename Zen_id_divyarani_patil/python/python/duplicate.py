def duplicate(inp3):
  dup = {}
  for i in range(inp3):
    dup +=1
    print(dup)

if __name__=="__main__":
  inp3 = {}
  for i in range(3):
    country =input("Enter a country name : ")
    currency =input("Enter a currency  : ")
    inp3[country] = currency
    print(inp3)