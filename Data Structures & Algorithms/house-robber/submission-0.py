class Solution:
    def rob(self, nums: list[int]) -> int:
        p1 = p2 = 0
        for i in nums:
            temp = max(p1 + i, p2)
            p1 = p2
            p2 = temp
        return temp