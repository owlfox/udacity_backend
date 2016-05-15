# User Instructions
#
# Implement the function escape_html(s), which replaces
# all instances of:
# > with &gt;
# < with &lt;
# " with &quot;
# & with &amp;
# and returns the escaped string
# Note that your browser will probably automatically
# render your escaped text as the corresponding symbols,
# but the grading script will still correctly evaluate it.
#

def escape_html(s):
    """
    >>> escape_html("test")
    'test'
    >>> escape_html('''&"test''')
    '&amp;&quot;test'
    """
    for (i, o) in (("&", "&amp;"), (">", "&gt;"), ("<", "&lt;"), ('"', "&quot;")):
        s = s.replace(i, o)
    return s

if __name__ == "__main__":
    import doctest
    doctest.testmod()
