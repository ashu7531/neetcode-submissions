class Solution:
    def rob(self, nums: list[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        def houserobber(idx, nums):
            p1 = p2 = 0
            temp = 0
            for i in nums:
                temp = max(p1 + i, p2)
                p1 = p2
                p2 = temp
            return temp
        ans = max(houserobber(0, nums[:len(nums) - 1]), houserobber(1, nums[1:]))
        return ans
