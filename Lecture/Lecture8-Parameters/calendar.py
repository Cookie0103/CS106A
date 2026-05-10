"""
File: calendar.py
-----------------
This program prints out a calendar, to show the days of the
week in each month.
"""

NUM_MONTHS = 12
NUM_DAYS_IN_WEEK = 7

"""
Functions given for free:
print_month_header(month)
format_number(num)
first_day_of_year(year)
"""

def main():
    """
    Prints calendar for the year entered by the user
    """
    year = int(input("Enter year for calendar: "))
    first_day = first_day_of_year(year)

    # TODO: your code here!


def print_month(first_day, month, year):
    """
    Prints a daily calendar for the given month and year.  It is
    also given the day of the week that this month starts on
    (0 = Sunday, 1 = Monday, ..., 6 = Saturday)

    Returns the day of the week that the *following* month would start on
    """
    # TODO: your code here!
    pass


def days_in_month(month, year):
    """
    Returns the number of days in the given month and year.
    Assumes that month 1 is January, month 2 is February, and so on.

    Doctests:
    >>> days_in_month(1, 2021)
    31
    >>> days_in_month(4, 2020)
    30
    >>> days_in_month(2, 1900)
    28
    >>> days_in_month(2, 2020)
    29
    """
    # TODO: your code here!
    pass


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
