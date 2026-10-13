class Solution:
    def numDecodings(self, s: str) -> int:
        # given string of digits and we need to return number of total ways that can be decoded

        # return 0 if digit starts with 0
        # if starts with 1 or 2 then check for diff cases
        # else pick only one case
        dp = {}

        def dfs(ind):
            if ind in dp:
                return dp[ind]
            if ind == len(s):
                return 1
            if s[ind] == '0':
                return 0
            res = 0
            if s[ind] == '1' or s[ind] == '2':
                # impletment later
                res += dfs(ind + 1)
                if (ind + 1) < len(s):
                    num = int(s[ind: ind+2])
                    if num <= 26:
                        res += dfs(ind+2)
            else:
                res += dfs(ind + 1)
            dp[ind] = res
            return res
        return dfs(0)


        