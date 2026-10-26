class Solution:
    def countSubstrings(self, s: str) -> int:
        count = 0
        n = len(s)
        dp = [[False] * (n + 1) for _ in range(n)]
        for length in range(1, n + 1):
            for start in range (n-length + 1):
                if length == 1:
                    dp[start][length] = True
                
                elif length == 2:
                    dp[start][length] = s[start] == s[start+length-1]

                else:
                    dp[start][length] = dp[start+1][length-2] and s[start] == s[length+start-1]

                if dp[start][length]:
                    count += 1

        return count

                