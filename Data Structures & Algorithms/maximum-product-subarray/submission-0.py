class Solution:
    def maxProduct(self, nums: list[int]) -> int:
        # 
        currMin = currMax = 1
        res = max(nums)

        for n in nums:
            if n == 0:
                currMin = currMax = 1
                continue
            tmp = currMax * n
            currMax = max(currMax * n, n * currMin, n)
            currMin = min(tmp, n * currMin, n)
            res = max(res, currMax)
        return res