import string

def ispangram(str1, alphabet=string.ascii.lowercase):
    alphaset = set(alphabet)
    print(alphaset <= set(str1.lower()))
ispangram("The quick brown fox jumps over the lazy dog")
