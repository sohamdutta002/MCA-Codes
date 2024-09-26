# Write a Python program to find the sum of even numbers in an integer array.
def sum_of_even_numbers(array):
    return sum([i for i in array if i % 2 == 0])

array = input("Enter the array: ").split()
array = [int(i) for i in array]
print("Sum of even numbers in the array: ", sum_of_even_numbers(array), end="")