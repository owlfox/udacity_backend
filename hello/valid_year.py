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
from __future__ import print_function
import string
def valid_year(year):
    """
    >>> valid_year('0') is None
    True
    >>> valid_year('-11') is None
    True
    >>> valid_year('1950')
    1950
    >>> valid_year('2000')
    2000
    >>> valid_year('foo') is None
    True
    >>> valid_year('10')
    10
    """
    if year:
        if type(year) is str:
            year = int(year) if year.isdigit() else None
        return year if year > 0 else None



if __name__ == "__main__":
    import doctest
    doctest.testmod()
