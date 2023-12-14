import re

# patterns = ['term1', 'term2']
#
# text = 'This is a string with term1, not the other'
#
# for pattern in patterns:
#     print("I'm searching for: " + pattern)
#
#     if re.search(pattern, text):
#         print("Match")
#     else:
#         print("Not match")


text = 'term1'
match = re.search('term1', text)
# To find the starting index of a match-
print(match.start())

# Regular Expressions also have the ability to split a sting on a particular pattern
split_term = '@'
email = 'user@gmail.com'
re.split(split_term, email)  # Out come ['user', 'gmail.com']

# Find all the instances of a pattern in a string
re.findall(split_term, email)


# Meta character syntax
def multi_re_find(patterns, phrase):
    for pat in patterns:
        print("Searching for {} pattern".format(pat))
        print(re.findall(pat, phrase))


# Repetition syntax- five ways to express repetition in patterns
test_phrase = 'sdsd..sssddd..sddsdd...dsds...dssssss...sddddd'

test_patterns = ['sd*']  # Looking for and s followed by 0 or more D's
# test_patterns = ['sd+']    -> Looks for an s followed by 1 or more D's
# test_patterns = ['sd?']    -> Looks for an s followed by 0 or 1 D
# test_patterns = ['sd{3}']    -> Looks for an s followed by 3 D's
# test_patterns = ['s[sd]+']    -> Looks for an s followed on or more D's and S's

multi_re_find(test_patterns, test_phrase)

test_phrase2 = 'This is a string! With punctuation. How do we remove that?'
test_pattern2 = ['[^!.?]']    # Find all, and remove then
# [r'\d+'] ->   gett all the numbers in a string
# [r'\D+'] ->   gett everything but numbers
# [r'\s+'] ->   sequence of white space



