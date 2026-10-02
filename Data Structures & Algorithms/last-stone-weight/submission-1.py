class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        if len(stones) == 1:
            return stones[0]
        heap = []
        heapq.heapify(heap)
        for stone in stones:
            heapq.heappush(heap, -stone)
        while len(heap) > 1:
            stone1 = -heapq.heappop(heap)
            stone2 = -heapq.heappop(heap)
            if stone1 != stone2:
                res = -abs(stone1 - stone2)
                heapq.heappush(heap, res)
        if heap:
            return -heap[0]
        else:
            return 0