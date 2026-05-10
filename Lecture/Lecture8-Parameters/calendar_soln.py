"""
File: calendar.py
-----------------
This program prints out a calendar, to show the days of the
week in each month.
"""

NUM_MONTHS = 12
NUM_DAYS_IN_WEEK = 7


def main():
    """
    Prints calendar for the year entered by the user
    """
    year = int(input("Enter year for calendar: "))
    first_day = first_day_of_year(year)
    for i in range(NUM_MONTHS):
        month = i + 1
        first_day = print_month(first_day, month, year)
        print('')


def print_month(first_day, month, year):
    """
    Prints a daily calendar for the given month and year.  It is
    also given the day of the week that this month starts on
    (0 = Sunday, 1 = Monday, ..., 6 = Saturday)

    Returns the day of the week that the *following* month would start on
    """
    print_month_header(month)
    n_days = days_in_month(month, year)

    # current line is a helper variable which stores the calendar line as we have built it so far.
    current_line = ''

    for i in range(first_day):
        current_line += '    '
    current_day_of_week = first_day

    for i in range(n_days):
        # recall that i starts counting at 0. Days start at 1
        day_index = i + 1
        # each day gets 4 spaces
        day_str = format_number(day_index)
        current_line += day_str
        current_day_of_week += 1
        if current_day_of_week == 7:
            # When you get to the day after Saturday, you must wrap the line!
            print(current_line)
            current_line = ''
            current_day_of_week = 0
    # Dont forget that there might be something left to print in the current line!
    if current_line != '':
        print(current_line)
    return current_day_of_week


def days_in_month(month, year):
    """
    Returns the number of days in the given month and year.
    Assumes that month 1 is January, month 2 is February, and so on.

    Doctests:
    >>> days_in_month(4, 2020)
    30
    >>> days_in_month(2, 1900)
    28
    """
    # Days in February depends on whether it's a leap year
    if month == 2:
        if is_leap_year(year):
            return 29
        else:
            return 28
    # April, June, September, November have 30 days
    elif month == 4 or month == 6 or month == 9 or month == 11:
        return 30
    # All other months have 31 days
    else:
        return 31


def is_leap_year(year):
    """
    Returns Boolean indicating if given year is a leap year.
    It is a leap year if the year is:
    * divisible by 4, but not divisible by 100
     OR
    * divisible by 400
    (Example of a "predicate function")

    Doctests:
    >>> is_leap_year(2001)
    False
    >>> is_leap_year(2020)
    True
    >>> is_leap_year(2000)
    True
    >>> is_leap_year(1900)
    False
    """
    # if the year is divisible by 400, it is a leap year!
    if is_divisible(year, 400):
        return True

    # other wise its a leap year if its divisible by 4 and not 100
    return is_divisible(year, 4) and not is_divisible(year, 100)


def is_divisible(a, b):
    """
    Returns a boolean which is True is the value in a is divisible by b
    """
    return a % b == 0

###################################################
#     Functions given to you for free! Enjoy      #
###################################################

def print_month_header(month):
    """
    Prints header for a given month in the calendar
    """
    print("Month #" + str(month))
    print("Sun Mon Tue Wed Thu Fri Sat")


def format_number(num):
    """
    Formats a one or two digit integer to fit in four spaces.
    Returns a string of the formatted number string.
    >>> format_number(12)
    ' 12 '
    >>> format_number(5)
    ' 5  '
    """
    result = " " + str(num) + " "
    if num < 10:
        result = result + " "
    return result


def first_day_of_year(year):
    """
    Returns the first day of the week for a given year, where
    (0 = Sunday, 1 = Monday, ..., 6 = Saturday)
    The formula in this function comes from http://mathforum.org/
    >>> first_day_of_year(2020)
    3
    """
    year -= 1
    return (year + (year // 4) - (year // 100) + (year // 400) + 1) % NUM_DAYS_IN_WEEK


# This provided line is required at the end of a Python file
# to call the main() function.
if __name__ == '__main__':
    main()
