# 1.The following is a list of 10 students ages:
# ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]
# I. Sort the list and find the min and max age
# II. Add the min age and the max age again to the list
# III. Find the median age (one middle item or two middle items divided by two)
# IV. Find the average age (sum of all items divided by their number )
# V. Find the range of the ages (max minus min)
# VI. Compare the value of (min - average) and (max - average), use _abs()_ method

#I
ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]
for i in range(len(ages)):
    for j in range(i+1, len(ages)):
        if ages[i] > ages[j]:
            ages[i], ages[j] = ages[j], ages[i]
print("Sorted ages: ", ages)
min_age = ages[0]
max_age = ages[-1]  
print("Min age: ", min_age)
print("Max age: ", max_age)

#II
ages.append(min_age)
ages.append(max_age)
print("List after adding min and max age: ", ages) 

#III
if len(ages)%2 == 0:
    median_age = (ages[len(ages)//2] + ages[len(ages)//2 - 1])/2
else:
    median_age = ages[len(ages)//2]
print("Median age: ", median_age)

#IV
average_age = sum(ages)/len(ages)
print("Average age: ", average_age)

#V
range_age = max_age - min_age
print("Range of ages: ", range_age)

#VI
min_average = abs(min_age - average_age)
max_average = abs(max_age - average_age)
print("Difference between min and average: ", min_average)
print("Difference between max and average: ", max_average)