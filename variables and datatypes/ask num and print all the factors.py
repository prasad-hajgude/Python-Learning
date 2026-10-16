#  ask the number from the user ,and print all the factors
# enter a number=10
# 1 2  5 10

# enter  a number =100
# 1,2, 4, 5 ,10 20 25 50 100

num=int(input("enter the number"))
i=1
count=0
while i<=num:
    if num %i==0:
     count=count+1
     print(i, end=" ")
    i+=1
print(f"total count of the number is = {count}")