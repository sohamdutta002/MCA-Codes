# Reverse the elements in an array of integers without using a second array.
def reverse_array(array):
    return array[::-1]  # Slicing the array from the end to the start

array = input("Enter the array: ").split()
array = [int(i) for i in array]
array = reverse_array(array)
print("Reversed array: ", array, end="")