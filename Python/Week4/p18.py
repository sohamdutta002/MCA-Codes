# Write a Python program to find duplicate elements in a 1D array and find their frequency of occurrence
def duplicate_elements(array):
    duplicates = []
    frequency = {}
    for i in array:
        if array.count(i) > 1 and i not in duplicates:  # array.count(i) returns the frequency of i in the array
            duplicates.append(i)
            frequency[i] = array.count(i)
    return duplicates, frequency

array = input("Enter the array: ").split()
array = [int(i) for i in array]
duplicates, frequency = duplicate_elements(array)
print("Duplicate elements in the array: ", duplicates)