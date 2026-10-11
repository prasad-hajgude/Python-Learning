# nested if-else statement means writing an if-else statement inside another if or else block.
# It is used when we need to check a condition first and then check another condition inside it.

# if condition1:
#     if condition2:
#         statement1
#     else:
#         statement2
# else:
#     statement3
# ex 
# age=45
# certificate =true

age=15
certificate=False

if age>=18:
    if certificate ==True:
        print("you will be hired")
    else:
        print("cannot be hired due to no certificate")
else:
    print("cananot hire due to age is less than 18")
