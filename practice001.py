
# 1) Write a program that takes a number as an input representing the day of the week 
# and checks whether that day is week.
def day_checker():
    weekday = int(input('Enter weekday number (1-7): '))

    if weekday in range(1, 6):
        print('\nWeekday\n');

    elif weekday in range(6, 8):
        print('\nWeekend\n')

    else:
        print('\nPlease enter any weekday number (1-7)\n')

day_checker()        