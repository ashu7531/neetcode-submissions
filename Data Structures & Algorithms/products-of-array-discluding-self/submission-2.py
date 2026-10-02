class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        # [1, 2, 3, 4]
        # [1, 1, 2, 6]
        # [24, 12, 4, 1]

        n = len(nums)

        output = [1] * n
        pre = 1

        for i in range(1, n):
            output[i] = pre * nums[i-1]
            pre = output[i]
        post = 1
        for j in range(n-2, -1, -1):
            post *= nums[j + 1]
            output[j] *= post
        return output