#  Write a Python program to calculate Sum of two 2-dimensional arrays.
def sum_of_2d_arrays(array1, array2):
    sum_array = []
    for i in range(len(array1)):
        sum_array.append([])
        for j in range(len(array1[i])):
            sum_array[i].append(array1[i][j] + array2[i][j])
    return sum_array

array1 = [[1, 2], [3, 4]]
array2 = [[5, 6], [7, 8]]
print("Sum of two 2-dimensional arrays: ", sum_of_2d_arrays(array1, array2), end="")