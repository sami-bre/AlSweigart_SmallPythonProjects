import datetime

MONTHS = ['January', 'February', 'March', 'April', 'May', 'June',
          'July', 'August', 'September', 'October']

print('This program outputs a printable table of a month.')
while True:
    print("Enter the year:")
    response = input('> ')

    if not response.isdecimal():
        print("please enter a numeric value, like 2021")
        continue

    year = int(response)
    if year > 0:
        break
    print("Please enter a number greater than 0.")

while True:
    print('Please enter the month: 1-12')
    response = input('> ')

    if not response.isdecimal():
        print("Please enter a numeric value")

    month = int(response)
    if 1 <= month <= 12:
        break
    print("Please enter a valid value specifying the month.")


def getCalText(yr, mnt):
    calText = ""
    weekLabel = '..Monday...Tuesday...Wednesday.Thursday...Friday...Saturday...Sunday..\n'
    weekSeparator = "+---------" * 7 + "+\n"
    blankRow = ("|" + (" " * 9)) * 7 + "|\n"

    currentDate = datetime.date(year=year, month=month, day=1)
    # roll back the current date until we hit monday
    while currentDate.weekday() != 0:
        currentDate -= datetime.timedelta(days=1)

    # let's make the calText
    calText += (" " * 32) + str(year) + " " + str(MONTHS[month - 1]) + "\n"
    calText += weekLabel
    calText += weekSeparator
    print(currentDate.month)
    print(month)
    while True:
        print("hey")
        weekLabelRow = ''
        for _ in range(7):
            weekLabelRow += ("|" + "{}".format(currentDate.day).rjust(2) + (" " * 7))
            currentDate += datetime.timedelta(days=1)
        weekLabelRow += "|\n"
        calText += weekLabelRow
        for _ in range(2):
            calText += blankRow
        calText += weekSeparator

        if currentDate.month != month:
            break

    return calText


if __name__ == '__main__':
    result = getCalText(year, month)
    print(result)

    fileName = "calendar_{}_{}".format(month, year)
    with open(fileName, 'w') as fileObj:
        fileObj.write(result)

    print("calendar text saved to {}".format(fileName))
