# A = {19, 22, 24, 20, 25, 26}
# B = {19, 22, 20, 25, 26, 24, 28, 27}
# 5. From the above sets A and B
# I. Join A and B
# II. Find A intersection B
# III. Is A subset of B
# IV. Are A and B disjoint sets
# V. Join A with B and B with A
# VI. What is the symmetric difference between A and B
# VII. Delete the sets completely

# I
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
A_B = A.union(B)
print("A union B: ", A_B)

# II
A_intersection_B = A.intersection(B)
print("A intersection B: ", A_intersection_B)

# III
A_subset_B = A.issubset(B)
print("Is A subset of B: ", A_subset_B)

# IV
A_B_disjoint = A.isdisjoint(B)
print("Are A and B disjoint sets: ", A_B_disjoint)

# V
A_B = A.union(B)
B_A = B.union(A)
print("A union B: ", A_B)
print("B union A: ", B_A)

# VI
symmetric_difference = A.symmetric_difference(B)
print("Symmetric difference between A and B: ", symmetric_difference)

# VII
del A
del B
print(A)
print(B)