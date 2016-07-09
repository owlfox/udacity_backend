
given_string = "I think %s is a perfectly normal thing to do in public."
def sub1(s):
    '''
    >>> sub1("running")
    'I think running is a perfectly normal thing to do in public.'
    >>> sub1("sleeping")
    'I think sleeping is a perfectly normal thing to do in public.'
    '''
    rtn = given_string % s
    return rtn

given_string2 = "I think %s and %s are perfectly normal things to do in public."
def sub2(s1, s2):
    '''
    >>> sub2("running", "sleeping")
    'I think running and sleeping are perfectly normal things to do in public.'
    >>> sub2("sleeping", "running")
    'I think sleeping and running are perfectly normal things to do in public.'
    '''
    return given_string2 % (s1, s2)

given_string3 = "I'm %(nickname)s. My real name is %(name)s, but my friends call me %(nickname)s."
def sub_m(name, nickname):
    '''
    >>> sub_m("Mike", "Goose")
    "I'm Goose. My real name is Mike, but my friends call me Goose."
    '''
    return given_string3 % {"name":name, "nickname":nickname}

# > with &gt;
# < with &lt;
# " with &quot;
# & with &amp;

escape_dict = {
'>':'&gt;',
'<':'&lt;',
'"':'&quot;',
'&':'&amp;',
}
def escape_html(s):
    '''
    >>> escape_html('>')
    '&gt;'
    >>> escape_html('<')
    '&lt;'
    >>> escape_html('"')
    '&quot;'
    >>> escape_html("&")
    '&amp;'
    '''
    rtn = ""
    for c in s:
        esp = escape_dict.get(c)
        if esp:
            rtn += esp
        else:
            rtn += c
    return rtn
