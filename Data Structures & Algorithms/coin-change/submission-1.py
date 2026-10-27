class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if amount == 0:
            return 0

        memo = {}
        def count(remaining) -> int:
            best = float('inf')
            if remaining == 0:
                return 0
            if remaining < 0:
                return float('inf')
            if remaining in memo:
                return memo[remaining]
            for coin in coins:
                best = min(best, 1 + count(remaining-coin))
            memo[remaining] = best

            return best

        final_count = count(amount)
        if final_count == float('inf'):
            return -1
        else:
            return final_count
        
                