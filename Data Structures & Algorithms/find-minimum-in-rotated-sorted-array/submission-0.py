class Solution:
    def findMin(self, nums: List[int]) -> int:
        start = 0
        end = len(nums) - 1

        while start <= end:
            mid = start + end - start
            # [7, 3]
            if mid < end and nums[mid] > nums[mid + 1]:
                return nums[mid + 1]
            # [7, 3, 4]
            if mid > start and nums[mid] < nums[mid - 1]:
                return nums[mid]
            if nums[mid] > nums[end]:
                start = mid + 1
            else:
                end = mid - 1
        return nums[0]