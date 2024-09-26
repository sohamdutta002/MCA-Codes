# Write a Python program to search an element in an array
def search_element(array, element):
    return element in array
array = input("Enter the array: ").split()
array = [int(i) for i in array]
element = int(input("Enter the element to be searched: "))
print("Element found: ", search_element(array, element), end="")