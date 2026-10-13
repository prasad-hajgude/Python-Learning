#  take the input from the user whertehr it is positive or negative or zero 
num=int(input("enter the number ="))
if  num>0:
    print("the number is positive")
elif num<0:
    print("the number is negative")
else:
    print("the number is zero")

#Q.8 take two numbers as input . print the greater of the two  . if they are equal , print "both are equal"
num1=int(input("enter the num1="))
num2=int(input("enter the number2="))
if num1>num2:
    print("num1 is greatest number")
elif num1==num2:
    print("both are equal")
else:
    print("num2 is greater")

#  take the year as leap year  a year is a leap year if it i dividable by 4 , but not by 100 , unless it is also divisible by 400 
year=int (input("enter the year="))
if year%400==0:
    print("the year is a leap year")
elif year%100==0:
    print("the year is not leap year")

elif year%4==0:
    print("the year is leap year")
elif year%100==0:
    print("the year is not leap year")




#  use ternary operator 
year = int(input("Enter year = "))

if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print("Leap year")
else:
    print("Not a leap year")