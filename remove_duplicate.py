def removeDuplicates(nums):
    count = 0
    result = []
    for i in range(0, len(nums)):
        if nums[i] != nums[i-1]:
            count += 1
            result.append(nums[i])
    return (str(count) + ", " + "nums = " + str(result))

nums = [0,0,1,1,1,2,2,3,3,4]
result = removeDuplicates(nums)
print(result)