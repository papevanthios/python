def square(num):
    print(num**2)
my_nums = [1,2,3,4,5]
for item in map(square, my_nums):
    print(item)


x = lambda num : num**2
list(map(x, my_nums))