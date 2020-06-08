"""
l=[1, 2, 3, 2, 1, 2], In this list which expression
can be used to find out number of '2' in the list?
"""

sample_list1 = [1, 2, 3, 2, 1, 2]

q = sample_list1.count(2)
print(q)

"""
Which expression(s) will print the last 2 elements of the list?
l=[1, 2, 3, 3, 2, 1] 
"""

l=[1, 2, 3, 3, 2, 1]

print(l[-2: ])
print(l[4:])
print(l[4:6])


custom_list1 = [2,3,4,5]
custom_list2 = ['a','b','c','d']

for i in custom_list2:
    custom_list1.append(i)

    print(custom_list1)

