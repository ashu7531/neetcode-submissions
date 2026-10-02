class Solution:
    def maxArea(self, heights: List[int]) -> int:
        start = 0
        end = len(heights) - 1
        maxArea = 0
        while start < end:
            area = min(heights[start], heights[end]) * (end  - start)
            if area > maxArea:
                maxArea = area
            if heights[start] <= heights[end]:
                start += 1
            else:
                end -= 1
        return maxArea
            