# 3.Create fruits, vegetables and animal products tuples.
# I. Join the three tuples and assign it to a variable called food_stuff_tp.
# II. Change the about food_stuff_tp tuple to a food_stuff_lt list
# III. Slice out the middle item or items from the food_stuff_tp tuple or food_stuff_lt list.
# IV. Slice out the first three items and the last three items from food_staff_lt list
# V. Delete the food_staff_tp tuple completely

# I
fruits = ('Apple', 'Banana', 'Orange')
vegetables = ('Carrot', 'Potato', 'Tomato')
animal_products = ('Milk', 'Egg', 'Meat')
food_stuff_tp = fruits + vegetables + animal_products
print("food_stuff_tp: ", food_stuff_tp)

# II
food_stuff_lt = list(food_stuff_tp)
print("food_stuff_lt: ", food_stuff_lt)

# III
middle_item = food_stuff_tp[len(food_stuff_tp)//2]  
print("Middle item: ", middle_item)

# IV
first_three = food_stuff_lt[:3]
last_three = food_stuff_lt[-3:]
print("First three items: ", first_three)
print("Last three items: ", last_three)

# V
del food_stuff_tp
print(food_stuff_tp) 