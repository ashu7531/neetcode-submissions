class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # Approach:
        # First i have to find the drop
        # Apply binary search in both half
        

        # Steps to find drop:
            # Find mid:
                # 1. If mid is lesser than end then shift end to mid - 1
                # 2, if mid is greater than end then shift start to mid + 1
        start = 0
        pivot = self.findDrop(nums)
        leftResult = self.binarySearch(nums[start:pivot], target)
        rightResult = self.binarySearch(nums[pivot:], target)
        if leftResult != -1:
            return leftResult
        elif rightResult != -1:
            return pivot + rightResult
        else:
            return -1

        
    def findDrop(self, nums):
        start = 0
        end = len(nums) - 1
        while start <= end:
            mid = start + (end - start)//2
            if mid < end and nums[mid] > nums[mid + 1]:
                return mid + 1
            if mid > start and nums[mid] < nums[mid - 1]:
                return mid
            if nums[mid] > nums[end]:
                start = mid + 1
            else:
                end = mid - 1
        return 0
    def binarySearch(self, nums, target):
        if not nums:
            return -1
        start = 0
        end = len(nums) - 1
        while start <= end:
            mid = start + (end - start)//2
            if target == nums[mid]:
                return mid 
            elif target < nums[mid]:
                end = mid - 1
            else:
                start = mid + 1
        return -1
        