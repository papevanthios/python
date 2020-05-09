

import string

def ispangram(str1, alphabet=string.ascii_lowercase):
    alphaset = set(alphabet)
    print(alphaset <= set(str1.lower()))
    print(string.ascii_lowercase)
ispangram("The quick brown fox jumps over the lazy dog")
