# Declare a function named print_list. It takes a list as a parameter and it prints out each element of the list. 

def print_list(lst):
    for i in lst:
        print(i)
    if len(lst) == 0:
        print('The list is empty')

lst = [1, 2, 3, 4, 5]
print_list(lst)