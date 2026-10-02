class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # Step 1: Count the frequency of each number
        countset = {}
        for num in nums:
            if num in countset:
                countset[num] += 1
            else:
                countset[num] = 1
        
        res = []
        
        # Step 2: Find the top K frequent elements
        while len(res) < k:
            max_freq = -1
            max_num = None
            
            # Step 3: Find the number with the highest frequency
            for num, freq in countset.items():
                if freq > max_freq:
                    max_freq = freq
                    max_num = num
            
            # Step 4: Append that number to the result and set its frequency to zero
            res.append(max_num)
            countset[max_num] = 0
        
        return res
