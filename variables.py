"""
'a' is the variable name,it is the reference to the object
'NYC' is the value of the object
"""

a= 'NYC'
b= 'NYC'

print(a)
#show that a and b access the same object with a single reference id
print(id(a))
print(id(b))
a=123

print(a)
print(b)

c='NYC'
d=c

print(c==d)
print(c is d)
print(d is c)
#List all the keywords that cannot be used as variable names
import keyword
print(keyword.kwlist)
