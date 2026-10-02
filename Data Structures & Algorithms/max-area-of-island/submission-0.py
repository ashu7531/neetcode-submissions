class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0
        rows = len(grid)
        cols = len(grid[0])
        visited = set()
        maxArea = 0
        def bfs(r, c):
            directions = [[0, 1], [1, 0], [0, -1], [-1, 0]]
            q = collections.deque()
            q.append((r, c))
            visited.add((r, c))
            area = 1
            while q:
                cr, cc = q.popleft()
                for dr, dc in directions:
                    nr = cr + dr
                    nc = cc + dc
                    if nr in range(rows) and nc in range(cols) and grid[nr][nc] == 1 and (nr, nc) not in visited:
                        visited.add((nr, nc))
                        q.append((nr, nc))
                        area += 1
            return area

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1 and (r, c) not in visited:
                    area = bfs(r, c)
                    if area > maxArea:
                        maxArea = area
        return maxArea
    