def h3(nums):
    for i in range (0,len(nums)-1):
        if nums[i] == 3 and nums[i+1] == 3:
            return True
    retur False
h3([1, 3, 1, 3])
h3([1, 3, 3])
