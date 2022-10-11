#1.Create a string, display it and check its data type

from re import X


str= 'python is easy'

print(str)
print(type(str))




'''2.Given the string :
      #s = "django"
Use indexing to print out the following:
‘d’ , ‘o’ , ’jan’ ,’djan’,’go’.
And Also reverse the above string.'''
s= "django"
print(s[0])
print(s[5])
print(s[1:4])
print(s[0:4])
print(s[-2:])
print(s[::-1])


'''3.Demonstrate following string methods on given string.
    S = '  Learning Python at LevelUp  '
        - remove white spaces of string from both ends
	- show the occurences of character in string
	- locate a substring
        - find the length of string
        - split the string into substrings
        - Represent the string in different cases
'''
s = '  Learning Python at LevelUp  '
print(s.strip())

print(s.count('n'))

print(s.find('Python'))

print(len(s))

print(s.split())

print(s.upper())
print(s.lower())
print(s.title())






'''4.Concatenate the following strings
     x="With Levelup I'm on cloud" + 9'''


x="With Levelup I'm on cloud"
y=' 9'
print(x+y)



#5.justify how strings are immutable 


levelup = 'cloud data engineer'

print(levelup)
levelup[0]='m'    #'str' object does not support item assignment



'''6.Find the length of string 
       #mystr = 'levelup Institute'''

mystr = 'levelup Institute'

print(len(mystr))



'''7.Using suitable string manipulation print the below output
             levelup levelup levelup '''

insti= ' levelup '
print(insti*3)         
