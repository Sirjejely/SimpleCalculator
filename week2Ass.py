"""
Create an empty list called my_list.
Append the following elements to my_list: 10, 20, 30, 40.
Insert the value 15 at the second position in the list.
Extend my_list with another list: [50, 60, 70].
Remove the last element from my_list.
Sort my_list in ascending order.
Find and print the index of the value 30 in my_list.
"""
my_list = [] #empty list
my_list.append(10) # append 10 to the list
my_list.append(20)
my_list.append(30)
my_list.append(40)
my_list.insert(1,15) # insert 15 at the second position
my_list.extend([50,60,70]) # extend the list
my_list.pop() # remove the last element
my_list.sort() # sort the list
print(my_list) # print the list
print(my_list.index(30)) # print the index of 30SS