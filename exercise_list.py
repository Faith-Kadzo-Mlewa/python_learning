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