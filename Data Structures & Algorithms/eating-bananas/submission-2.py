class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        max_val = float("-inf")
        for pile in piles:
            if pile > max_val:
                max_val = pile
        condition = True
        start = 1
        end = max_val
        res = end
        while start <= end:
            mid = start + (end - start)//2
            time = 0
            for pile in piles:
                time += math.ceil(pile/mid)
            if time <= h:
                res = mid
                end = mid - 1
            if time > h:
                start = mid + 1
        return res

          


