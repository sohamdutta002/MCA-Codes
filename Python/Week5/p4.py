# 4. Create a set given below
# it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
# age = [22, 19, 24, 25, 26, 24, 25, 24]
# I. Find the length of the set it_companies
# II. Add 'Twitter' to it_companies
# III. Insert multiple IT companies at once to the set it_companies
# IV. Remove one of the companies from the set it_companies
# V. What is the difference between remove and discard

#I
it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
print("Length of it_companies: ", len(it_companies))

#II
it_companies.add('Twitter')
print("it_companies after adding Twitter: ", it_companies)

#III
it_companies.update(['TCS', 'Infosys'])
print("it_companies after adding TCS and Infosys: ", it_companies)

#IV
it_companies.remove('TCS')
print("it_companies after removing TCS: ", it_companies)

#V
# remove() raises an error if the element is not present in the set, whereas discard() does not raise an error.