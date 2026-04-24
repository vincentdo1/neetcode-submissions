class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        ROWS, COL = len(grid), len(grid[0])
        count = 0
        def bfs(i, j):
            if (i < 0 or i >= ROWS or j < 0 or j >= COL or grid[i][j] == "0"):
                return
            else:
                grid[i][j] = "0"
                bfs(i, j + 1)
                bfs(i, j - 1)
                bfs(i + 1, j)
                bfs(i - 1, j)
            return

        for i in range(ROWS):
            for j in range(COL):
                if (grid[i][j] == "1"):
                    bfs(i, j)
                    count += 1
        return count