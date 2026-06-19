# dictionary:its a collection of keys value pairs
marks={
    "dayasagar":340,
    "sunayana":400,
    "kabita":500,
    "barsha":460
}
print(marks)
print(marks["sunayana"])

# properties:unordered,mutable,indexed,can not contain duplicate key
# dictionary method
'''print(marks.items())
print(marks.values())
print(marks.keys())
marks.update({"sunayana":450})
print(marks)
print(marks.get("kabita"))
marks.pop("barsha")
print(marks)
marks["badal"]=300
print(marks)
marks.popitem()
print(marks)
d1={"a":1}
d2=d1.copy()
print(d2)
marks.update(d1)
print(marks)'''

# set:its collection of well defined object and it contain non repeate element
s={1,2,3,4,2,3,5}
print(s)
# set methods
s.add(6)
print(s)
s.update([7,8,9])
print(s)
s.remove(9)
print(s)
s.discard(10)
print(s)
s.pop()
print(s)
x=s.copy()
print(x)
# a=[1,2,3,5,"daya"]
# print(list(set(a)))
# set operation
# union(|)or(union())
a={1,2,3,4}
b={5,6,7}
print(a|b)
print(a.union(b))
# intersection(&)or(intersection())
print(a&b)
print(a.intersection(b))
# difference(-)
print(a-b)
print(a.difference(b))
# symmetric difference(^)
print(a^b)
# membership operator(in)
print(4 in a)
# issubset()
print(a.issubset(b))
# issuperset
print(b.issuperset(a))
# isdisjoint
print(b.isdisjoint(a))