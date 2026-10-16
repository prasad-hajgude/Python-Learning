#  sum of 1 to 100 and divisible by 2 and 7
start=int(input("enter the start number="))
end=int(input("enter the end number="))

i=start
total=0
while i<=end:
    if i%2==0 and i%7==0:
     print(i, end=" ")
     total=total+i
    i+=1
    

print(f"total={total}")
    