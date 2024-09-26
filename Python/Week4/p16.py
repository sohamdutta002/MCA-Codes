#  Write a Python program to enter n elements in an array and find smallest number among them
def smallest_number(array):
    return min(array)

array = input("Enter the array: ").split()
array = [int(i) for i in array]
print("Smallest number in the array: ", smallest_number(array), end="")