"""Calendar Maker, by Al Sweigart al@inventwithpython.com
Calendar Maker -- mini vers., modified by Nihat Halici
Create monthly calendars, saved to a text file and fit for printing.
View this code at https://nostarch.com/big-book-small-python-projects
Tags: short"""

import datetime

# Set up the constants:
DAYS = ('Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday',
        'Friday', 'Saturday')
MONTHS = ('January', 'February', 'March', 'April', 'May', 'June', 'July',
          'August', 'September', 'October', 'November', 'December')

print('Calendar Maker, by Al Sweigart al@inventwithpython.com')

# Loop to get a year from the user.
while True:
    print('Enter the year for the calendar:')
    response = input('> ')

    if response.isdecimal() and int(response) > 0:
        year = int(response)
        break

    print('Please enter a numeric year, like 2023.')
    continue

# Loop to get a month from the user.
while True:
    print('Enter the month for the calendar, 1-12:')
    response = input('> ')

    if not response.isdecimal():
        print('Please enter a numeric month, like 3 for March.')
        continue

    month = int(response)
    if 1 <= month <= 12:
        break

    print('Please enter a number from 1 to 12.')


def getCalendarFor(year, month):
    # calText will contain the string of our calendar.
    calText = ''

    # Put the month and year at the top of the calendar:
    calText += (' ' * 8) + MONTHS[month - 1] + ' ' + str(year) + '\n'
    
    # Add the days of the week labels to the calendar
    calText += '.Su..Mo..Tu..We..Th..Fr..Sa..\n'

    # The horizontal line string that separate weeks:
    weekSeparator = ('+---' * 7) + '+\n'

    # The blank rows have ten spaces in between the | day separators:
    blankRow = ('|  ' * 7) + '|\n'

    # Get the first date in the month. (The datetime module handles all
    # the complicated calendar stuff for us here.)
    currentDate = datetime.date(year, month, 1)

    # Roll back currentDate until it is Sunday. (weekday() returns 6
    # for Sunday, not 0.)
    while currentDate.weekday() != 6:
        currentDate -=  datetime.timedelta(days = 1)

    # Loop over each week in the month.
    while True:
        calText += weekSeparator

        # dayNumberRow is the row with the day number labels:
        dayNumberRow = ''
        for i in range(7):
            dayNumberLabel = str(currentDate.day).rjust(2)
            dayNumberRow += '|' + dayNumberLabel + (' ' * 1)
            currentDate += datetime.timedelta(days = 1)  # Go to next day.
        dayNumberRow += '|\n'  # Add the vertical line after Saturday.

        # Add the day number row and 3 blank rows to the calendar text.
        calText += dayNumberRow
        for i in range(0):
            calText += blankRow

        # Check if we're done with the month:
        if currentDate.month != month:
            break

    # Add the horizontal line at the very bottom of the calendar.
    calText += weekSeparator
    return calText

calText = getCalendarFor(year, month)
print(calText)  # Display the calendar.

# Save the calendar to a text file:
calendarFilename = 'calendar_mini_{}_{}.txt'.format(year, month)
with open(calendarFilename, 'w') as fileObj:
    fileObj.write(calText)

print('Saved to ' + calendarFilename)
