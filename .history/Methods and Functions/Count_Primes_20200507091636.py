def cp(num):
    if num < 2:
        return 0
    
    primes = [2]
    x = 3

    while x <= num:
        for y in range(e,x,2):
            if x%y == 0:
                x += 2
                break
        else:
            primes.append(x)
            x += 2
    print(primes)
    print(len(primes))

    cp(100)