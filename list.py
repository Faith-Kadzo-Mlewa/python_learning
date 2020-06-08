"""
Data Type that stores more than one value in one variable name
List items are in brackets separated by "," [1, 2, 3]

List is mutable because we can add and modify elements to and from the same list
even after creation
"""
cars = ['bmw', 'range-rover', 'Audi']
print(cars)

#Empty List
empty_list=[]
print(empty_list)

#Accessing element in a list

print(cars[0])
print(cars[1])
print(cars[2])

print( '*' * 10)

#A multidimentional list(By nesting a list inside another list
multidim = [[1, 2], 'one', [3, 4], 'three']
print(multidim)
print(multidim[0][1])
print(multidim[3])
print(multidim[2][0])

print( '*' * 10)

#Numbers list operations
numb_list = [1, 2, 3, 4]
sum_num = numb_list[0] +numb_list[3]
print(sum_num)
modulo_num = numb_list[2] % numb_list [1]
print(modulo_num)
div_numb = numb_list[2] // numb_list[1]
print(div_numb)

#Re-assigning list values using indices
makeup = ['powder', 'foundation', 'blush']
print(makeup)

makeup[1] = 'eyeshadow'
print(makeup[1])
print(makeup)

#Check the ID of an object in lists

days = ['Monday', 'Tuesday', 'Wednesday']
print(id(days))
print(id(days[0]))
print(id(days[1]))
print(id(days[2]))

days[1] = 'Saturday'
print(days)
print(id(days[1]))
print(id(days))
print(id(days[0]))

#Changing the element in a list means the new item is stored in a different memory address


print('*' *20)
"""
List Methods
"""
#Length
weekdays = ['Monday', 'Tuesday', 'Wednesday', 'Thursday']
print(weekdays)

list_length = len(weekdays)
print(list_length)

#append() method - Adds elements to the end of the list
weekdays.append('Friday')
print(weekdays)

#insert() method - Adds elements to a desired index. Has 2 arguments (position,value)
weekdays.insert(2, 'Saturday')
print(weekdays)

#index() method - Find index of a particular item in a list
x = weekdays.index("Saturday")
print(x)

#extend() method - Adds multiple elements at the same time at the end of the list
alphabets = ['a', 'b', 'c', 'd', 'e']
print(alphabets)

alphabets.extend([1, 2, 3])
print(alphabets)

#pop() method - Removes the last item from the list unless its given a particular index value.
#When a particular index value is given then the element in that index will be removed
y=weekdays.pop()
print(y)

print(weekdays)

#remove() method - Used to remove an item whose value is stated. Only removes an element at a time
#remove() method will only remove the first occurence of the searched element
weekdays.remove("Tuesday")
print(weekdays)

#to remove multiple elements in a list, an iterator has to be used
remov_list = [1,2,3,3,4,4,5,6,7,8]
print(remov_list)
for i in range(1,5):
    remov_list.remove(i)
print(remov_list)

print('*' *20)
"""
Slicing a list
First Index is inclusive, Last Index is Exclusive
"""
digit_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print(digit_list)

slice1 = digit_list[2:]
print(slice1)

slice2 = digit_list[3:8]
print(slice2)

#skip 2 steps
slice3 = digit_list[3:8:2]
print(slice3)

print("Printing the entire list in reverse order")
slice4 = digit_list[::-1]
print(slice4)
print('*' *20)

"""
Sorting a list
"""
a = ['Alex', 'Zoe', 'Faith', 'Anita','Taurus']
print(a)

#sort() in ascending order by default
a.sort()
print(a)

#sort in descending order
a.sort(reverse=True)
print(a)

print('*' *20)

"""
Count() method. Counting the number of occurrence of an item in a list
"""
occurance = ['a', 'b', 'c', 'd', 'a', 'c', 'a', 'b', 'b']
print(occurance.count('a'))
print(occurance.count('b'))
print(occurance.count('d'))
print(occurance.count('c'))
