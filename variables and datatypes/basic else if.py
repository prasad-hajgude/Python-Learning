# if elif else statement - it is used when more the two possible outcomes can possible
# python checks each conditions from top to botto then if one is that true then it can executes it and the entire are skipped 
# Syntax

# if condition1:
#     statement1
# elif condition2:
#     statement2
# elif condition3:
#     statement3
# else:
#     statement4

# 90 and above --> A 
# 81-90 --> B
# 71-80 --> C 
# 61-70--> D
# 60 and below   --> fail

marks=int(input("enter the marks "))
if marks>=90 and marks<=100:
    print("grade A")
elif marks>=81 and marks<=90:
    print("garde b")
elif marks>=71 and marks<=80:
    print("grade c")
elif marks>=61 and marks<=70:
    print("grade d")
elif marks>=45 and marks<=60:
    print("grade e")
elif marks>=0 and marks<=45:
    print("fail")

else:
    print("invalid marks ")
