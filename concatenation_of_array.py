def getConcatenation(nums):
        ans = []
        for i in range(len(nums)):
            ans.append(nums[i])
        return ans + ans
       
                 
nums = [0,1,2]
result = getConcatenation(nums)
