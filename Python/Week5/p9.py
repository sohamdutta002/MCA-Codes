# 9. Print the season name of the year based on the month number using a dictionary.

month = int(input("Enter month number: "))
seasons = {
    1: 'Winter',
    2: 'Winter',
    3: 'Spring',
    4: 'Spring',
    5: 'Spring',
    6: 'Summer',
    7: 'Summer',
    8: 'Summer',
    9: 'Autumn',
    10: 'Autumn',
    11: 'Autumn',
    12: 'Winter'
}
if(month < 1 or month > 12):
    print("Invalid month number")
else:
    print("Season: ", seasons[month])