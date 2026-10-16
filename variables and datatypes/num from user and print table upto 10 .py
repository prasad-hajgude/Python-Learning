#  ask a number frm the user , print the multiplication table upto 1 to 10 

# enter a number=4
# then output is 
# 4*1=4
# 4*2=8 that type of theoutput
num=int(input("enter the number="))
i=1
while i<=10:
    ans=num*i
    print(f"{num}* {i}={ans}")
    i+=1