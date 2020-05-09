def rc(num, low, high):
    if num >= low and num <= high:
        print(f'{num} is between {low} and {high}')

def rb(num,low,high):
    if num >= low and num <= high:
        return True


rc(5,2,7)
rb(5,2,7)