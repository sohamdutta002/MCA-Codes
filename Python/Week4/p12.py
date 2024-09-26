# Write a Python program to find the range of a 1D array. means the difference between the maximum and minimum element in the array. example: if array is [1, 2, 3, 4, 5], then range is 5 - 1 = 4.
def range_of_array(array):
    return max(array) - min(array)

array = input("Enter the array: ").split()
array = [int(i) for i in array]
print("Range of the array: ", range_of_array(array), end="")