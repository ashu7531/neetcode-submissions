from collections import deque
class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        ans = []
        rows = len(heights)
        cols = len(heights[0])
        for r in range(rows):
            for c in range(cols):
                if self.reachPacific(r, c, heights) and self.reachAtlantic(r, c, heights):
                    ans.append([r, c])
        return ans
    def reachPacific(self, r, c, heights):
        directions = [[0, 1], [0,-1], [1, 0], [-1, 0]]
        q = deque()
        q.append([r,c])
        visited = set()
        while q:
            cr, cc = q.popleft()
            if self.PacificRange(cr, cc, heights):
                return True
            for ar, ac in directions:
                nr = ar + cr
                nc = ac + cc
                if nr in range(len(heights)) and nc in range(len(heights[0])) and heights[nr][nc] <= heights[cr][cc] and (nr, nc) not in visited:
                    q.append([nr, nc])
                    visited.add((nr, nc))
        return False
            

    def reachAtlantic(self, r, c, heights):
        directions = [[0, 1], [0,-1], [1, 0], [-1, 0]]
        q = deque()
        q.append([r,c])
        visited = set()
        while q:
            cr, cc = q.popleft()
            if self.AtlanticRange(cr, cc, heights):
                return True
            for ar, ac in directions:
                nr = ar + cr
                nc = ac + cc
                if nr in range(len(heights)) and nc in range(len(heights[0])) and heights[nr][nc] <= heights[cr][cc] and (nr, nc) not in visited:
                    q.append([nr, nc])
                    visited.add((nr, nc))
        return False

    def PacificRange(self, r, c, heights):
        if r == 0 or c == 0:
            return True
        return False
    def AtlanticRange(self, r, c, heights):
        if r == len(heights) - 1 or c == len(heights[0]) - 1:
            return True
        return False
    