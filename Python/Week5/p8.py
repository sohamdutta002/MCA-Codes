# 8.Create a person dictionary.
# person={
# 'first_name': 'Asabeneh',
# 'last_name': 'Yetayeh',
# 'age': 250,
# 'country': 'Finland',
# 'is_marred': True,
# 'skills': ['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
# 'address': {
# 'street': 'Space street',
# 'zipcode': '02210'
# }
# }
# I. Check if the person dictionary has skills key, if so print out the middle skill in the skills list.
# II. Check if the person dictionary has skills key, if so check if the person has 'Python' skill and print out the result.
# III. If a person skills has only JavaScript and React, print('He is a front end developer'), if the person skills has Node, Python, MongoDB, print('He is a backend developer'), if the person skills has React, Node and MongoDB, Print('He is a fullstack developer'), else print('unknown title') - for more accurate results more conditions can be nested!
# IV. If the person is married and if he lives in Finland, print the information in the following
# format:
# ```py
# Asabeneh Yetayeh lives in Finland. He is married.
# ``

person={
'first_name': 'Asabeneh',
'last_name': 'Yetayeh',
'age': 250,
'country': 'Finland',
'is_marred': True,
'skills': ['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
'address': {
'street': 'Space street',
'zipcode': '02210'
}
}

# I
if 'skills' in person:
    middle_skill = person['skills'][len(person['skills'])//2]
    print("Middle skill: ", middle_skill)

# II
if 'skills' in person:
    if 'Python' in person['skills']:
        print("Person has Python skill")
    else:
        print("Person does not have Python skill")

# III
if 'skills' in person:
    if person['skills'] == ['JavaScript', 'React']:
        print("He is a front end developer")
    elif 'Node' in person['skills'] and 'Python' in person['skills'] and 'MongoDB' in person['skills']:
        print("He is a backend developer")
    elif 'React' in person['skills'] and 'Node' in person['skills'] and 'MongoDB' in person['skills']:
        print("He is a fullstack developer")
    else:
        print("Unknown title")

# IV
if person['is_marred'] == True and person['country'] == 'Finland':
    print(person['first_name'], person['last_name'], "lives in", person['country'], ". He is married.")