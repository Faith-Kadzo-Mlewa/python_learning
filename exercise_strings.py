"""Assume you have a string, a = "one two three".

How can you put the items of the string into a list?

Example: l = ['one', 'two', 'three']

"""
a = "one two three"
my_list = a.split(" ")
print(my_list)

"""
What are the different ways to retrieve 'c' in the string, x='abc'? 

"""

x = 'abc'

print(x[2])
print(x[-1])


"""
Which expression(s) will output "I am loving python language"

a="am"

b="language"
"""
a = 'am'
b = 'language'

print("I " + a + " loving python " +b)
print("I %s loving python %s" %(a,b))

"""
Write a Python program to calculate the length of a string.
"""
input_string = input("Enter the name of your city: ")
print(input_string)

print("Your city is " + str(len(input_string)) + " characters long")

"""
NOT DONE, to review later after having learnt dictionary
Write a Python program to count the number of characters (character frequency) in a string.
Sample String : google.com'
Expected Result : {'o': 3, 'g': 2, '.': 1, 'e': 1, 'l': 1, 'm': 1, 'c': 1}
"""
sample_string1 = "google.com"

"""
Write a Python program to get a string made of the first 2 
and the last 2 chars from a given a string.If the string length is less than 2, 
return instead of the empty string. 
Sample String : 'w3resource'
Expected Result : 'w3ce'
Sample String : 'w3'
Expected Result : 'w3w3'
Sample String : ' w'
Expected Result : Empty String 
"""
derived_string = input("Enter a string: ")

print(derived_string[:2] + derived_string[-2:])

"""
Write a Python program to get a string from a given string where all occurrences of its first char have been changed to '$',
except the first char itself. 
Sample String : 'restart'
Expected Result : 'resta$t'
Sample String 2 : 'google.com'
Expected Result :  'go$gle.c$m'
"""
sample_string2 = 'restart'
my_char = sample_string2[0]
changed_string1 = sample_string2.replace(my_char,"$")
sample_string2 = my_char + changed_string1[2:]

print(sample_string2)


sample_string3 = 'google.com'
my_char2 = sample_string3[1]
changed_string2 = sample_string3.replace(my_char2,"$")
sample_string3 = sample_string3[0] + my_char2 + changed_string2[2:]

print(sample_string3)

