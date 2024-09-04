# Declare a function named reverse_list. It takes an array as a parameter and it returns the reverse of the array (use loops).

def reverse_list(lst):
    while (len(lst) > 0):
        print(lst.pop())

lst = [1, 2, 3, 4, 5]
reverse_list(lst)