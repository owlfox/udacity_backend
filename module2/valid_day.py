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
    '''
    >>> valid_day('0') is None
    True
    >>> valid_day('1')
    1
    >>> valid_day('15')
    15
    >>> valid_day('500') is None
    True
    '''
    rtn = None
    if day and day.isdigit() is True:
        num = int(day)
        if num <= 31 and num >= 1:
            rtn = num
    return rtn
