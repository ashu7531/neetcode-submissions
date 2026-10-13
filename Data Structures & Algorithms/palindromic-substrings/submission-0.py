class Solution:
    def countSubstrings(self, s: str) -> int:
        n = len(s)
        if n == 0:
            return 0
        ans  = 0
        dp = [[False] * n for _ in range(n)]
        

        for i in range(n):
            dp[i][i] = True
            ans += 1

        for length in range(2, n + 1):
            for i in range(n - length + 1):
                j = i + length - 1

                if s[i] == s[j]:
                    if length <= 3:
                        dp[i][j] = True
                    else:
                        dp[i][j] = dp[i + 1][j - 1]

                if dp[i][j]:
                    ans += 1

        return ans
