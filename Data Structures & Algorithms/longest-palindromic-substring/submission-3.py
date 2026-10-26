class Solution:
    def longestPalindrome(self, s: str) -> str:
        max_len = 0
        longest_start = 0
        n = len(s)
        dp = [[False] * (n + 1) for _ in range(n)]
        for length in range(1, n + 1):
            for start in range(n - length + 1):
                if length == 1:
                    dp[start][length] = True

                elif length == 2:
                    dp[start][length] = s[start] == s[start+1]
                
                else:
                    dp[start][length] = dp[start+1][length-2] and (s[start] == s[start+length-1])

                if dp[start][length] and length > max_len:
                    longest_start = start
                    max_len = length
        return s[longest_start:longest_start + max_len]
