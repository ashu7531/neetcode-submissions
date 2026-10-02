class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        if not grid:
            return None

        rows, cols = len(grid), len(grid[0])
        directions = [[0, -1], [-1, 0], [0, 1], [1, 0]]
        q = collections.deque()

        # Step 1: Add all cells with value 0 to the queue
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 0:
                    q.append((r, c))

        # Step 2: Perform a level-wise BFS
        dist = 0
        while q:
            dist += 1
            for _ in range(len(q)):  # Process all cells at the current distance
                cr, cc = q.popleft()
                for dr, dc in directions:
                    nr, nc = cr + dr, cc + dc
                    if nr in range(rows) and nc in range(cols) and grid[nr][nc] == 2147483647:
                        grid[nr][nc] = dist  # Update distance for this cell
                        q.append((nr, nc))
