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

def valid_month(month):
    '''
    >>> valid_month("january")
    'January'
    >>> valid_month("January")
    'January'
    >>> valid_month("foo") is None
    True
    >>> valid_month("") is None
    True
    '''
    rtn, caped_Mon = None, None
    if month:
        caped_Mon = month.capitalize()
        if caped_Mon in months:
            i = months.index(caped_Mon)
            rtn = months[i]
    return rtn
#
# print valid_month("january")
# # => "January"
# print valid_month("January")
# # => "January"
# print valid_month("foo")
# # => None
# print valid_month("")
# # => None
