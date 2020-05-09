def unl(lst):
    x = []
    for i in lst:
        if i not in x:
            x.append(i)
    print(x)
unl([2,3,5,1])

    