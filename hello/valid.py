# -----------
# User Instructions
#
# Modify the valid_month() function to verify
# whether the data a user enters is a valid
# month. If the passed in parameter 'month'
# is not a valid month, return None.
# If 'month' is a valid month, then return
# the name of the month with the first letter
# capitalized.
#
from __future__ import print_function
from valid import *
import logging

months = ['January',
          'February',
          'March',
          'April',
          'May',
          'June',
          'July',
          'August',
          'September',
          'October',
          'November',
          'December']

month_abbvs = dict((m[:3].lower(),m) for m in months)

def valid_month(month):
    """
    Simply use https://docs.python.org/2/library/string.html#string.capitalize
    >>> valid_month("january")
    'January'
    >>> valid_month("foo") is None
    True
    >>> valid_month("Dec")
    'December'
    >>> valid_month("dec")
    'December'
    """
    return month_abbvs.get(month[:3].lower()) # pretty neat!




# -----------
# User Instructions
#
# Modify the valid_day() function to verify
# whether the string a user enters is a valid
# day. The valid_day() function takes as
# input a String, and returns either a valid
# Int or None. If the passed in String is
# not a valid day, return None.
# If it is a valid day, then return
# the day as an Int, not a String. Don't
# worry about months of different length.
# Assume a day is valid if it is a number
# between 1 and 31.
# Be careful, the input can be any string
# at all, you don't have any guarantees
# that the user will input a sensible
# day.
#
# Hint: The string function isdigit() might be helpful.

def valid_day(day):
    """
    >>> valid_day('0') is None
    True
    >>> valid_day('-11') is None
    True
    >>> valid_day('foo') is None
    True
    >>> valid_day(10)
    '10'
    """
    day = str(day)
    if day and day.isdigit():
            day = int(day)
            return  str(day) if day<32 and day>0 else None
    else:
        return None






# -----------
# User Instructions
#
# Modify the valid_year() function to verify
# whether the string a user enters is a valid
# year. If the passed in parameter 'year'
# is not a valid year, return None.
# If 'year' is a valid year, then return
# the year as a number. Assume a year
# is valid if it is a number between 1900 and
# 2020.
#


def valid_year(year):
    """
    >>> valid_year('0') is None
    True
    >>> valid_year('-11') is None
    True
    >>> valid_year('1950')
    '1950'
    >>> valid_year('2000')
    '2000'
    >>> valid_year(1999)
    '1999'
    >>> valid_year('foo') is None
    True
    >>> valid_year('10') is None
    True
    """
    year = str(year)
    if year and year.isdigit():
        year = int(year)
        return str(year) if 2020 > year > 1900 else None
    else:
        return None




if __name__ == "__main__":
    import doctest
    doctest.testmod()
