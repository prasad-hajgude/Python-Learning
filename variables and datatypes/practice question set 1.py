#  take two numbers as input from the user , print their sum , differnece product  and remainder 
num1=int(input("enter the num1="))
num2=int(input("enter the number2="))
add=num1+num2
sub=num1-num2
multiplication =num1*num2
remainder=num1%num2
print(add)
print(sub)
print(multiplication)
print(remainder)

#  using f string format
print(f"sum={num1+num2}")
print(f"sub={num1-num2}")
      

# take the number aas input , print whether it is even or odd using the % opeerator and a comparison operator
#  even  when the num is divided by 2 then the remainder is 0 that is called even and the number is divided by 2 then remainder is 0 then it is called as the odd 
num=int(input("enter the number ="))
print(num%2==0)

#  take the user age as input check whether they are eleigible to vote (age>=18) and whether they are a senior citizen (age>=60)print both results.

age=int(input("enter the age is="))
can_vote=age>=18
can_senior_citizen=age>60
print(f"can vote={can_vote}")
print(f"can senior citizen={can_senior_citizen}")


#  a student scored  a marks in 3 subject . take all three as input , calculate the total and averagr , and print both using  an f-string 
sub1=int(input("enter the marks in sub1="))
sub2=int(input("enter the marks in sub 2="))
sub3=int(input("enter the marks in sub3="))

avg=total/3
total=sub1+sub2+sub3
print(f"avg={avg:.2f}marks and the total={total}marks")
