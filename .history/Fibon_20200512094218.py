'''
Fibonacci
'''
from HeaderFiles import Header1

def gen_fibon(n):
    '''
    Seq
    '''

    a = 1
    b = 1
    for i in range(n):
        yield a
        a,b = b,a+b

list(gen_fibon(10))
