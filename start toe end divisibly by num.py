#  print the start and even number divisible by 3 and 4
start=int(input("enter the start number="))
end=int(input("enter the end number="))
i=start
while i<=end:
    if i%3==0 and i%4==0:
        print(i,end=" ")
    i+=1
