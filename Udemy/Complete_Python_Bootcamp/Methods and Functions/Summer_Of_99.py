def s99(arr):
    total = 0
    add = True

    for num in arr:
        while add:
            if num != 6:
                total += num
                break
            else:
                add = False
        while not add:
            if num != 9:
                break
            else:
                add = True
                break
    print(total)
s99([1,3,5])
s99([1,2,6,7,8,9,10])
s99([6,9,0])