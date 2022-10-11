'''1. Given the nested list:
   l=[2,3,[1,6,'Java']]
   Reassign 'Java' to 'Python'.'''

from re import L


l =[2,3,[1,6,'Java']]
print(l)
l[2][2]='python'
print(l )


   
#2.Demonstrate working of copy function for list.  
 

l1=['python',43]
print(l1)
l2= l1.copy()
print(l2)


'''3.Join the below two lists
  l1=[1,2,3]
  l2=[4,5,6]'''

l1=[1,2,3]
l2=[4,5,6]
print(l1+l2)
   
#4.Create list using constructor. 
mani = list((1,2,3,4,5))
print(mani)
print(type(mani))



 
'''5.Given list:
  lst=['w','e','l','c','o','m','e']
  demonstrate list membership test.'''
lst=['w','e','l','c','o','m','e']

print('e' in lst)

print('o' not in lst)




'''6.Given the list
  l1=[1,2,3,'abc',4,5,6]
     - perform indexing to print 'abc'
     - perform slicing to print 4,5
     - perform negative indexing
     - add an element to list
     - add an element specific position in list
     - remove an element of list
     - pop specific element of list'''


l1=[1,2,3,'abc',4,5,6]
print(l1)
print(l1[3])

print(l1[4:6])

print(l1[-4:-1])

l1.append(8)
print(l1)

l1.insert(3,4)
print(l1)

l1.remove('abc')
print(l1)

l1.pop(3)
print(l1)



'''7.
   lst=['a','b',1,2,3,4]
         - reverse the list
         - sort the list in ascending and descending order
         - print the list lst twice
         - print the max and min element from the list'''
lst=['a','b',1,2,3,4]
print(lst[::-1])

print(lst)

lst.pop(0)
lst.pop(0)
print(lst)

lst.sort()
print(lst)
lst.sort(reverse=True)
print(lst)

print(lst*2)

print(max(lst))
print(min(lst))