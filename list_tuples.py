# lists:its a containerto store a set of value of any datatype
friends=["daya","sagar","majhi",3,5,7,2.5,True]
"""print(friends[0])
friends[7]=False
print(friends[7])
print(friends[1:8]
for i in friends:
    print(i)"""

# list methods
"""friends.append("mrunal")
print(friends[8])"""

"""num=[0,1,7,2,4,5,3,10,14]
num.sort()
print(num)
num.reverse()
print(num)
num.insert(4,66)
print(num)
num.pop(2)
print(num)
num.remove(66)
print(num)
num.extend([7,"sm",90])
print(num) """

# tuples:itsan immutable datatype its stores in collection same as list
"""a=(3,4,4,5,4)
print(type(a))
# tuples method
no=a.count(4)
print(no)
b=a.index(4)
print(b)"""

# must use tuples operation
# accesing element
'''a=(10,20,30)
print(a[-1])
print(a[0])'''

# slicing
a=(2,3,7,"s","e","x","y")
print(a[0:5])

# length
b=("faa","oo",7,9)
print(len(b))

# membeership check
print("fa" in b)

# iterate
for i in a:
    print(i)

# packing&unpacking:it packing multiple values into a single tuple
c=(1,3,4,5)
print(c)
d,e,f,g=c
print(d)
print(e)
print(f)
print(g)
h,*i,j=c
print(h)
print(*i)
print(j)
