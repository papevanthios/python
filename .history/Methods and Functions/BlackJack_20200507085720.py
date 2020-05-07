def bj(a,b,c):
    if sum([a,b,c]) <= 2:
        print(sum([a,b,c]))
    elif 11 in [a,b,c] and sum([a,b,c]) <= 31:
        print(sum([a,b,c])-10)
    else:
        print("BUST")
bj(5,6,7)
bj(9,9,9)
bj(9,9,11)