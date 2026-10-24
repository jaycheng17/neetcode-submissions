class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        length = len(nums)
        prefix = [0] * length
        suffix = [0] * length

        prefix[0] = nums[0]

        suffix[length - 1] = nums[length - 1]
        for i in range(1, length):
            prefix[i] = nums[i] * prefix[i-1]
        for j in range(length - 2,-1,-1):
            suffix[j] = nums[j] * suffix[j+1]
            
        result = [0] * length
        for i in range(0,length):
            if i == 0:
                result[i] = suffix[i + 1]
            elif i == length - 1:
                result[i] = prefix[i-1]
            else:
                result[i] = prefix[i-1] * suffix[i+1]
        
        return result

