'''
Fibonacci
'''

def gen_fibon(n):
    '''
    Seq
    '''

    a = 1
    b = 1
    for _ in range(n):
        yield a
        a,b = b,a+b

print(list(gen_fibon(10)))
