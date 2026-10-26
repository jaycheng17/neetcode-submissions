class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        house_list1 = nums[1:]
        house_list2 = nums[:-1]
        return max(self.robLinear(house_list1),self.robLinear(house_list2))

    def robLinear(self,nums: List[int]) -> int:
        memo = [-1] * len(nums)
        def dp(n):

            if n >= len(nums):
                return 0
            if memo[n] != -1:
                return memo[n]
            memo[n] = max(nums[n] + dp(n+2),dp(n+1)) 
            return memo[n]
        
        return dp(0)
