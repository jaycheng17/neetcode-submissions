class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        result,i = [],0
        for i in range(len(nums)):
            count = 1
            j = 0
            for j in range(len(nums)):
                if j == i:
                    continue
                else:
                    count *= nums[j]
            result.append(count)
        return result