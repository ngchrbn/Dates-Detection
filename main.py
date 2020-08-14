"""
Date Detection uses regular expression to detect dates in the DD/MM/YYYY format.
Then it verifies the validity of a date:
                        ==> 31/02/2020 doesn't exist but it is detected as a date
❗ Note that if the day or month is a single digit, it'll have a leading zero.
"""

# All imports
import datetime
import re

# Hold variable used to check if a detected year is great than the current year(if we are in 2020, there can't be 2021)
now = datetime.datetime.now()
current_year = now.year

# Dict used to map numbered month to their actual name
months = {
    '01': 'January', '02': 'February', '03': 'March', '04': 'April', '05': 'May', '06': 'June',
    '07': 'July', '08': 'August', '09': 'September', '10': 'October', '11': 'November', '12': 'December'
}
invalid_dates = {}  # Hold invalid dates and the reason for being invalid


# Function that uses a regex to detect a date in DD/MM/YYYY format
def detect_date(text):
    with open(f'{text}') as file_obj:
        content = file_obj.read()
        date_regex = re.compile(r'\d\d/\d\d/\d\d\d\d')
        dates = date_regex.findall(content)
    return dates


# Usages: Check if the dates in the list are all valid and retain the valid ones only
def validate_date(list_of_dates):
    """Check if the dates in list are valid which means:
        example: ==> February has 29 or 28 days depending on the year, etc
    """
    if len(list_of_dates) == 0:  # check if the list empty
        print('There is no date detected!')
    else:
        for i, _ in enumerate(list_of_dates):
            # split the string in day, month, year and for each  day, month and year if check they are valid
            # Append the invalid ones to the new dictionary
            day, month, year = _.split('/')
            if month in ['01', '03', '05', '07', '08', '10', '12']:
                if int(day) > 31:
                    invalid_dates[_] = f'{months[month]} can\'t have more than 31 days'
            elif month in ['04', '06', '09', '11']:
                if int(day) > 30:
                    invalid_dates[_] = f'{months[month]} can\'t have more than 31 days'
            elif month == '02':
                if int(year) % 4 == 0:
                    if int(day) > 29:
                        invalid_dates[_] = f'{months[month]} can\'t have more than 29 days when it is a leap year'
                else:
                    if int(day) > 28:
                        invalid_dates[_] = f'{months[month]} can\'t have more than 29 days when it is not a leap year'
            if int(year) > current_year:
                invalid_dates[_] = f'We are not yet in {year}'
    # After validating the dates, remove the invalid ones from list_of_dates
    for _ in invalid_dates.keys():
        if _ in list_of_dates:
            list_of_dates.remove(_)

# User Menu
print('Welcome to the date detection program'.center(60, '-'))
file = input('Enter a .txt file to detect dates inside it: ')
dates_list = detect_date(file)
validate_date(dates_list)
if len(invalid_dates) > 0:
    print('WARNING'.center(13, '!'))
    print('Some dates detected are invalid..')
    print('Here is the list of the invalid dates')
    for _, reason in invalid_dates.items():
        print(_, '==>', reason)
    print('Here is the list of the valid dates detected')
    for _ in dates_list:
        print(_, sep=', ')
else:
    print('Here is the list of the dates detected')
    for _ in dates_list:
        print(_)
