#function:its a group of statements performing a specific task
# to find average of 3 numbers
'''def avg():
    a=int(input("enter a number"))
    b=int(input("enter a number"))
    c=int(input("enter a number"))
    avg=(a+b+c)/3
    print(avg)
avg()'''

'''def arg(name,ending):
    print("good morning",name)
    print(ending)
arg("daya","thank you")'''

# recursion:it is a function which calls itself
def factorial(n):
    if (n==1 or n==0):
        return 1
    return n*factorial(n-1)
n=int(input("enter a number"))
print(f"the factorial of {n}is {factorial(n)}")
    