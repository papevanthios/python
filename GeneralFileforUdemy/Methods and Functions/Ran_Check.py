def rac(num, low, high):
    if num > low and num < high:
        print(f'{num} is between {low} and {high}')

def rab(num,low,high):
    if num >= low and num <= high:
        print(True)


rac(5,2,7)
rab(5,2,7)