class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        # take a maxheap and insert first k elements(index, dist)
        # now iterate over rest of arr and insert the element if distance is smaller than
        # top element otherwise leave
        # keep poping elements from heap and insert it in result arr
        heap = []
        heapq.heapify(heap)
        for i in range(k):
            ind = i
            dist = -math.sqrt(points[i][0]**2 + points[i][1]**2)
            heapq.heappush(heap, [dist, ind])
        for i in range(k, len(points)):
            ind = i
            dist = -math.sqrt(points[i][0]**2 + points[i][1]**2)
            if -dist < -heap[0][0]:
                heapq.heappop(heap)
                heapq.heappush(heap, [dist, ind])
        res = []
        for i in heap:
            ind = i[1]
            res.append(points[ind])
        return res

            

        