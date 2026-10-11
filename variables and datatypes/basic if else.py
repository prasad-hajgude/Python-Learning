#  if else -it is conditionl statemnet used to make decisions in python  if the condition is true i=then if block executes and then if dalse the else block executes 
#  syntax 
# if condition:
#     statement

# else:
#     statement

#  check eligible to vote or not 
age=int(input("enter the age of the voter="))
if age>=18:
    print("elgible to vote")

else:
    print("not eligible to vote")

print("done")


#  check the student is fail or pass 
physics=int(input("enter the physics marks "))
chemistry=int(input("enter the chemistry marks "))

if physics>33 and chemistry>33:
    print("student is pass")

else:
    print("student is fail ")
print("apply for photocopy revaluation")