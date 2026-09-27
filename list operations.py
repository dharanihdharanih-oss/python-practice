# 2b) Write a program to create a list and perform the following operations
# 1) Inserting an element
# 2) Removing an element
# 3) Appending an element
# 4) Displaying the length of the list
# 5) Popping an element
# 6) Clearing the list

my_list = [15, 25, 35, 45, 55]
print("Initial list:", my_list)

my_list.insert(5, 60)
print("List after inserting 60 at position 5:", my_list)

my_list.remove(25)
print("List after removing an element:", my_list)

my_list.append(78)
print("List after adding 78 to the end of my_list:", my_list)

list_length = len(my_list)
print("Length of the list:", list_length)

popped_element = my_list.pop()
print("Popped element is:", popped_element)
print("List after popping an element:", my_list)

my_list.clear()
print("List after clearing:", my_list)