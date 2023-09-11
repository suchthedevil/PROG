
def twoSum(nums,target):
    for i,j in enumerate(nums):
        unknown = target - j
        i1 = i
        for k,l in enumerate(nums):
            if l == unknown:
                i2 = k
                break
    print([i1,i2])

twoSum([2,7,11,15],9)


        
