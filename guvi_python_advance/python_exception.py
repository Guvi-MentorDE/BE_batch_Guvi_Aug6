a = 10
b = 0
print("Result of Division: " + str(a/b))

if(amount > 2999)
print("You are eligible to purchase Dsa Self Paced")

try:
    a = 10
    b = 0
    print("Result of Division: " + str(a/b))
except:
    print("You have divided a number by zero, which is not allowed.")
    

# try block with multiple except
try:
    a = int(input("Enter numerator number: "))
    b = int(input("Enter denominator number: "))
    print("Result of Division: " + str(a/b))
# except block handling division by zero
except(ZeroDivisionError):
    print("You have divided a number by zero, which is not allowed.")
# except block handling wrong value type
except(ValueError):
    print("You must enter integer value")
# generic except block
except:
    print("Oops! Something went wrong!")
 



# try - except - finally 
#finally - which is always executed after the try and except blocks
try:
    a = 10
    b = 1
    print("Result of Division: " + str(a/b))
# except block handling division by zero
except(ZeroDivisionError):
    print("Result of Division: " + str(a/b))
finally:
    print("Code execution Wrap up!")
    
    
#try - except - raise
a = 10
b = 0
try:
    print(a/b)
except ZeroDivisionError:
    raise


from cmath import e


try:
    a = 10
    b = 'hi'
    print("Result of Division: " + str(a/b))
# except block handling division by zero
except e:
    print("Result of Division: ", e)
finally:
    print("Code execution Wrap up!")