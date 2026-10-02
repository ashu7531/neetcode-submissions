class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        visited = set()
        for i in range(len(nums)):
            for j in range(len(nums)):
                for k in range(len(nums)):
                    if i != j and i != k and j != k:
                        if nums[i] + nums[j] + nums[k] == 0:
                            triplet = tuple(sorted([nums[i], nums[j], nums[k]]))
                            if triplet not in visited:
                                res.append(list(triplet))
                                visited.add(triplet)
        return res