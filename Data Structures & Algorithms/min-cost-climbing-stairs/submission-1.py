class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        memo = {}

        def climb(n):
            if n >= len(cost):
                return 0
            if n in memo:
                return memo[n]
            memo[n] = cost[n] + min(climb(n+1),climb(n+2))
            return memo[n]
        
        return min(climb(0),climb(1))