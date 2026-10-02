class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        # [1, 2, 3, 4]
        # [1, 1, 2, 6]
        # [24, 12, 4, 1]

        n = len(nums)

        prefix = [1] * n
        suffix = [1] * n

        for i in range(1, n):
            prefix[i] = prefix[i-1] * nums[i-1]
        for j in range(n-2, -1, -1):
            suffix[j] = suffix[j + 1] * nums[j + 1]
        res = []
        for t in range(n):
            res.append(suffix[t] * prefix[t])
        return res