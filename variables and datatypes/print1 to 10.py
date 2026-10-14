#  print 1 to 10 numbers 


i=1
while i<=10:
    print(i,end=" ")
    i+=1


#  start and end by the user 
#  print start toe nd using while loop

start=int(input ("enter the start number="))
end=int(input("enter the end number="))
i=start

while i <= end:
  print(i,end=" ")
  i+=1

print(f"after while loop , start value is {start}")

#  start to end print even numbers 

start =int (input("enter the start number="))
end=int(input("enter the end number ="))

i=start
while i<=end:
    if i%2==0:
     print(i, end=" ")
    i+=1