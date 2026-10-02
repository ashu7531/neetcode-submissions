class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        #Approach
        # I will keep two list one will keep track of multiplication of elements after the curr ind.
        # Other will keep track of multiplication of elements upto curr ind.
        # prenums = []
        # mul = 1
        # for num in nums:
        #     prenums.append(mul)
        #     mul *= num
        # postnums = []
        # mul = 1
        # for num in nums[::-1]:
        #     postnums.append(mul)
        #     mul *= num
        # postnums = postnums[::-1]
        # res = []
        # for i in range(len(nums)):
        #     res.append(prenums[i] * postnums[i])
        # return res

        # Other Approach
        # I will initialise a variable with val = 1 and a res list and will start iteration 
        # on nums and will keep inserting val of prefix and will update prefix by multiplying with curr
        # num.
        # Same thing i will do another time for postfix but i will start iteration 
        # backward.
        res = [1] * len(nums)
        prefix = 1
        for i in range(len(nums)):
            res[i] = prefix
            prefix *= nums[i]
        postfix = 1
        for i in range(len(nums)-1, -1, -1):
            res[i] *= postfix
            postfix *= nums[i]
        return res