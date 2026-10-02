class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        countset = {}
        for num in nums:
            if num in countset:
                countset[num] += 1
            else:
                countset[num] = 1
        res = []
        holder = k
        while k > 0:
            max_freq = 0
            for val in countset.values():
                if val > max_freq:
                    max_freq =  val
            for key in countset:
                if countset[key] == max_freq and len(res) < holder:
                    res.append(key)
                    countset[key] = 0
            k -= 1
        return res