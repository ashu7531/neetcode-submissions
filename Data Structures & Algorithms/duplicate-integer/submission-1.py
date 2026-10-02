class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # Approach
        # 1. Start iterating and store element in hashset while inserting check
        # if it is already in array in or not.
        # my_set = set()
        # for num in nums:
        #     if num in my_set:
        #         return True
        #     else:
        #         my_set.add(num)
        # return False
        if len(set(nums)) == len(nums):
            return False
        return True
         