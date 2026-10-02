class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        pointer = 0
        while pointer < len(nums):
            if nums[pointer] == pointer + 1 or nums[pointer] == 0:
                pointer += 1
            else:
                temp = nums[pointer]
                nums[pointer] = nums[temp - 1]
                nums[temp - 1] = temp
        pointer2 = 0
        while pointer2 < len(nums):
            if nums[pointer2] == 0:
                return pointer2 + 1
            pointer2 += 1
        return 0
            
            
                 