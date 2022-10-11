#1.use a set to find the unique values of list :

 #mylist = [2,2,2,2,2,2,6,6,6,6,6,3,3,3,3,3,3]

from locale import DAY_2


mylist = [2,2,2,2,2,2,6,6,6,6,6,3,3,3,3,3,3]
print(set(mylist))

'''2.Given a set,demostrate the use of copy().

   s={"fb","insta","twitter","whatsapp"}''' 
s={"fb","insta","twitter","whatsapp"}
print(s)
s2=s.copy()
print(s2)
s2=set(s)
print(s2)

#3.create set and demonstrate the use of difference(),subset(),superset(),intersection.
m={1,2,3,3,3,45}
n={1,2,3,4,6,7,8}
o=m.difference(n)
print(o)
o=n.difference(m)
print(o)

o=m.issubset(n)
print(o)
o=m.issuperset(n)
print(o)

o=m.intersection(n)
print(o)

#4.create a set and convert it into frozenset.

y={'socula','shed'}

print(y)

z=frozenset(y)
print(type(z))


#5.show how two sets can be joined with an example.

m1 = {12,3,4,6,7}
m2={3,4,5,6,2}
m3= m1.union(m2)

print(m3)

