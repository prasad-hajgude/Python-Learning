# sum of all numbers from 1 to 100

start=int(input("enter the start number="))
end=int(input("enter the end number="))

i=start
total=0
while i<=end:
    total=total+i
    i+=1

print(f"total = {total}")
