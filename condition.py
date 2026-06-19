age=int(input("enter your age"))
if age%2==0:
    print("age is even")
if age>=18:
    print("u can drive")
elif age<18 and age>0:
    print("u can't drive")    
else:
    print("invalid")
