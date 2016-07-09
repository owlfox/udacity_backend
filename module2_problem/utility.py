import re
USER_RE = re.compile(r"^[a-zA-Z0-9_-]{3,20}$")
PW_RE = re.compile(r"^.{3,20}$")
EMAIL_RE = re.compile(r"^[\S]+@[\S]+.[\S]+$")

def valid_username(username):
    '''
    >>> valid_username("taaasdas") is None
    False
    >>> valid_username("ta") is None
    True
    >>> valid_username("dsa_") is None
    False
    '''
    return USER_RE.match(username)
def valid_email(email):
    return EMAIL_RE.match(email)
def valid_pw(pw):
    return PW_RE.match(pw)


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

def rot13(s):
    '''
    >>> rot13("abc")
    'nop'
    >>> rot13("ABC,.")
    'NOP,.'
    '''
    rtn = ""
    for c in s:
        c_i = ord(c)
        #upper case
        if c_i >= 65 and c_i <=90:
            c_i = c_i - 13 if c_i > 77 else  c_i + 13
        #lower case
        elif c_i >= 97 and c_i <=122:
            c_i = c_i - 13 if c_i > 109 else  c_i + 13
        rtn += chr(c_i)
    return rtn
