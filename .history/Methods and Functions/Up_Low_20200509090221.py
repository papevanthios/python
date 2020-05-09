def upl(s):
    upper = 0
    lower = 0
    for i in s:
        if i.isupper():
            upper += 1
        else:
            lower += 1
    print(f'No. of Upper case characters : {upper}')
    print(f'No. of Lower  case characters : {lower}')
upl("sss sss sss S")
