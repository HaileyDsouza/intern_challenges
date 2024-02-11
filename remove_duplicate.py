def removeDuplicates(nums):
    count = 0
    for i in range(0, len(nums)):
        if nums[i] != nums[i-1]:
            nums[count] = nums[i]
            count += 1
    return count

nums = [0,0,1,1,1,2,2,3,3,4]
result = removeDuplicates(nums)
print(result)

""" 
Given an integer array nums sorted in non-decreasing order, remove the duplicates in-place such that each unique element appears only once. 
The relative order of the elements should be kept the same. Then return the number of unique elements in nums.
"""
