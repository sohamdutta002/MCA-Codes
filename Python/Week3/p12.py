# Write a python script that displays the following table
# 1 1 1 1 1
# 2 1 2 4 8
# 3 1 3 9 27
# 4 1 4 16 64
# 5 1 5 25 125


def display_table():
    for n in range(1, 6):
        print(f"{n:<2} 1  {n:<2} {n**2:<4} {n**3:<4}")

display_table()
