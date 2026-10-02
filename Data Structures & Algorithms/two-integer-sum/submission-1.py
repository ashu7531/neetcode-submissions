class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # Approach:
        # Iterate through array and check if difference of current with target exists in set or not otherwise element with index.
        storage = {}
        for idx, num in enumerate(nums):
            diff = target - num
            if diff in storage:
                return [storage[diff], idx]
            storage[num] = idx
        