def lote(a,b):
    if a%2 == 0 and b%2 == 0:
        print(min(a,b))
    else:
        print(max(a,b))
        
lote(2,5)
lote(2,4)


#  min(a, b) returns the minimum of the two 
#  max(a, b) returns the maximum of the two