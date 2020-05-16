from HeaderFiles import Header1
import statistics

def squares(l,m,s):
    for i in range(s):
        yield ( m - l[i] )**2

print('Δώσε όσους αριθμούς θες! Για να σταματήσεις δώσε κάποιον χαρακτήρα')
try: 
    my_list = []     
    while True: 
        my_list.append(int(input()))          
except: 
    print(my_list)
sm = sum(my_list)


for x in squares(my_list,statistics.mean(my_list),len(my_list)):
    print(x)
