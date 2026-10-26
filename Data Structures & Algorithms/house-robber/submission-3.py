class Solution:
    def rob(self, nums: List[int]) -> int:
        memo = [-1] * len(nums)
        def dp(n):
            if n >= len(nums):
                return 0
            if memo[n] != -1:
                return memo[n]
            memo[n] = max(nums[n] + dp(n+2),dp(n+1)) 
            return memo[n]
        
        return dp(0)