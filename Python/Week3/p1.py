# Write a function called check-season, it takes a month parameter and returns the season: Autumn, Winter, Spring or Summer.  

def check_season(month):
    if month in ['December', 'January', 'February']:
        return 'Winter'
    elif month in ['March', 'April', 'May']:
        return 'Spring'
    elif month in ['June', 'July', 'August']:
        return 'Summer'
    elif month in ['September', 'October', 'November']:
        return 'Autumn'
    else:
        return 'Invalid Month'

month = input('Enter the month: ')
print(check_season(month))