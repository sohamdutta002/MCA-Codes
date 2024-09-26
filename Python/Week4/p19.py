# Write a Java program to print every alternate number of a given array. step by step
def alternate_numbers(array):
    return [array[i] for i in range(0, len(array), 2)] 

array = list(map(int, input("Enter the array: ").split())) # Taking input as a list of integers then converting it to a list & storing it in array
print("Alternate numbers in the array: ", alternate_numbers(array), end="")