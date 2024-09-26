# 7. Create a student dictionary and add first_name, last_name, gender, age, marital status, skills,
# country, city and address as keys for the dictionary
# I. Get the length of the student dictionary
# II. Get the value of skills and check the data type, it should be a list
# III. Modify the skills values by adding one or two skills
# IV. Get the dictionary keys as a list
# V. Get the dictionary values as a list
# VI. Change the dictionary to a list of tuples using _items()_ method
# VII. Delete one of the items in the dictionary
# VIII. Delete one of the dictionariesk

student ={}
student['first_name'] = 'Atrika'
student['last_name'] = 'Show'
student['gender'] = 'Female'
student['age'] = 22
student['marital status'] = 'Single'
student['skills'] = ['Java', 'Javascript']
student['country'] = 'India'
student['city'] = 'Howrah'
student['address'] = 'Howrah, West Bengal'

# I
print("length of student dictionary: ", len(student))

# II
print("Type of skills: ", type(student['skills']))

# III
student['skills'].append('Python')
student['skills'].append('C++')
print("Modified skills: ", student['skills'])

# IV
keys = list(student.keys())
print("Keys as list: ", keys)

# V
values = list(student.values())
print("Values as list: ", values)

# VI
items = list(student.items())
print("Dictionary as list of tuples: ", items)

# VII
del student['city']
print("Dictionary after deleting city: ", student)

# VIII
del student
print(student)