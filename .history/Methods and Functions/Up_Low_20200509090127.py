def upl(s):
    upper = 0
    lower = 0
    for i in s:
        if i.isupper():
            upper += 1
        else:
            lower += 1
upl("sss sss sss S")
