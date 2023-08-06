
#If - else 
#if - else - elseif 
#nested if else statements 
#indendation. python is a indend based prog lang

if condition is true:
    <i will execute if true>
else: 
    <i wll execute if false>
    
    
if 2 is even:
    print("even")
else: 
    print("odd")
    
    
if <condition>:
    statement
    


#-----
#case:  (specail - switch)   


age = int (input("Enter your age to check eligiblity to vote? "))  
if age>=18:  
    print("You are eligible to vote !!");  
else:  
    print("Sorry! you have to wait !!");  
    
number = int(input("Enter the number?"))  
if number==10:  
    print("number is equals to 10")     #logic cond 1 
elif number==50:  
    print("number is equal to 50")      #logic cond  
elif number==100:  
    print("number is equal to 100")     #logic cond 3
else:                                       #default ; nothing above is true this exexutes
    print("number is not equal to 10, 50 or 100");  
    

number1 = int(input("Enter the number?")) 
if number1%2==0:
    print("number is even")
#else:
    #print("odd or prime number")
 
#Nested if - else 

#operators 
#> < = 
#str1 == str2
#!=  

time = int(input("enter the time:")) hello 

if (time >= 600) and (time < 1200):
	print ("Morning");
else:
	if (time == 1200):
		print ("Noon");
	else:
		if (time > 1200) and (time <= 1700):
			print ("Afternoon");
		else:
			if (time > 1700) and (time <= 2000):
				print ("Evening");
			else:
				if ((time > 2000) and (time < 2400)) or ((time >= 0) and (time < 600)):
					print ("Night");
				else:
					print ("Invalid time!");


#case expression
lang = input("What's the programming language you want to learn? ")

match lang:
    case "JavaScript":
        print("You can become a web developer.")

    case "Python":
        print("You can become a Data Scientist")

    case "PHP":
        print("You can become a backend developer")
    
    case "Solidity":
        print("You can become a Blockchain developer")

    case "Java":
        print("You can become a mobile app developer")
    case _:
        print("The language doesn't matter, what matters is solving problems.")  #mandatory


