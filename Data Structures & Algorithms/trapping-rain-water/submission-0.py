class Solution:
    def trap(self, height: List[int]) -> int:
        if not height or len(height) < 3:
            return 0
        maxLeft = [0] * len(height)
        maxRight = [0] * len(height)
        maxLeftVal = float ("-inf")
        for i in range(1, len(height)):
            if height[i-1] > maxLeftVal:
                maxLeftVal = height[i-1]
            maxLeft[i] = maxLeftVal
        maxRightVal = float ("-inf")
        for i in range(len(height) - 2, -1, -1):
            if height[i+1] > maxRightVal:
                maxRightVal = height[i+1]
            maxRight[i] = maxRightVal
        res = 0
        for i in range(len(height)):
            val = min(maxLeft[i], maxRight[i]) - height[i]
            if val > 0:
                res += val
        return res