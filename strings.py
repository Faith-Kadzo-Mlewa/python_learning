
"""
Strings : Sequence of characters
contains a-z , 0-9, special characters e.g. @
Must be enclosed in single or double quotes

"""

a = "This is a sample string"
b = 'Strings also use single quotes'

print(a)
print(b)

#use of quotes within a string

c = "Need to use 'quotes' inside a string"
print(c)

d = "Second way to handle \"quotes\" in a string"
print(d)

e = "This is a \
 single string"
print(e)

f = 'This is \"Reader\'s\" digest'
print(f)

"""
String methods in python
"""

#Accessing the characters in a string
#Index start from zero

my_string = "Faith"
print(my_string[3])

my_string2 = my_string[2]
print(my_string2)

"""
String methods: len() , lower(), upper(), str()
"""
stri= "This Is a Mixed Case Sentence"
print(stri.lower())
print(stri.upper())
print(len(stri))

#Typcasting of an int to a string value
print(stri + str(2))

"""
String Concatenation
"""
print("Hello " +my_string+ " " + stri)

#Replace a pattern or a char in a string using replace method

a = '1abc2abc3abc4abq'
b = a.replace('abc', 'ABC')
c = a.replace('abc', 'ABC', 1)
d = a.replace('abc', 'ABC', 2)

print(b)
print(c)
print(d)

print("**********")
#Substrings

"""
#Single character from a string
Index in a string start from Zero (0)
"""
substri1 = a[3]
print(substri1)


"""
#Multiple characters from a string
Starting Index is inclusive
Ending Index is exclusive
Arguments here include [starting index : ending index : Steps]
Steps is the number of character(s) to skip then print the next one. Default value is 1
"""
#a = '1abc2abc3abc4abq'
substri2 = a[2:8]
print(substri2)

#Examples of step:

substri3 = a[2:8:1] #default value of 1
print(substri3)

substri4 = a[2:9:2] #step value 2
print(substri4)
substri5 = a[2:9:3] #Step value 3
print(substri5)

substri6 = a[-1:-2]
print(substri6)

"""
Want to replace is with was in the sentence below but do not
want to replace the "is" contained in the word This. 
"""
b = "This is my first Python programming"
c = (b.replace(" is", " was"))
print(c)


