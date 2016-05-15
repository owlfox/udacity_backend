# User Instructions
#
# Write a function 'sub1' that, given a
# string, embeds that string in
# the string:
# "I think X is a perfectly normal thing to do in public."
# where X is replaced by the given
# string.
# The function should return the new string.

given_string = "I think %s is a perfectly normal thing to do in public."
def sub1(s):
    return given_string %(s)


print sub1("running")
# => "I think running is a perfectly normal thing to do in public."
print sub1("sleeping")
# => "I think sleeping is a perfectly normal thing to do in public."



# User Instructions
#
# Write a function 'sub2' that, given two
# strings, embeds those strings in the string:
# "I think X and Y are perfectly normal things to do in public."
# where X and Y are replaced by the given
# strings.
# The function should return the new string.

given_string2 = "I think %s and %s are perfectly normal things to do in public."
def sub2(s1, s2):
    return given_string2 %(s1, s2)


print sub2("running", "sleeping")
# => "I think running and sleeping are perfectly normal things to do in public."
print sub2("sleeping", "running")
# => "I think sleeping and running are perfectly normal things to do in public."


# User Instructions
#
# Write a function 'sub_m' that takes a
# name and a nickname, and returns a
# string of the following format:
# "I'm NICKNAME. My real name is NAME, but my friends call me NICKNAME."
#

given_string2 = "I'm %(nickname)s. My real name is %(name)s, but my friends call me %(nickname)s."
def sub_m(name, nickname):
    return given_string2 %{"nickname":nickname, "name":name}



print sub_m("Mike", "Goose")
# => "I'm Goose. My real name is Mike, but my friends call me Goose."
