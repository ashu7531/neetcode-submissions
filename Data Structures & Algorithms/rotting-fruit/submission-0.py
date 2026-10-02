class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        if not grid:
            return None
        rows = len(grid)
        cols = len(grid[0])
        q = collections.deque()
        directions = [[0, -1], [-1, 0], [0, 1], [1, 0]]
        minute = -1
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 2:
                    q.append([r, c])
        while q:
            for _ in range(len(q)):
                r, c = q.popleft()
                for dr, dc in directions:
                    cr = r + dr
                    cc = c + dc
                    if cr in range(rows) and cc in range(cols) and grid[cr][cc] == 1:
                        grid[cr][cc] = 2
                        q.append([cr, cc])
            minute += 1
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    return -1 
        return max(0, minute)       