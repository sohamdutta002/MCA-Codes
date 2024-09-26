# Write a Java program which counts the non-zero elements in an integer array
def count_non_zero_elements(array):
    return len([i for i in array if i != 0])

array = list(map(int, input("Enter the array: ").split())) # Taking input as a list of integers then converting it to a list & storing it in array
print("Number of non-zero elements in the array: ", count_non_zero_elements(array), end="")