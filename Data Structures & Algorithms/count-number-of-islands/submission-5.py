class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        #iterate through the grid until we find a 1
        #then, do dfs on the 1 and mark them as 'x' 
        #when we do this we iterate the count
        #return this count once over
        rows = len(grid)
        cols = len(grid[0])
        def dfs(r, c):
            if grid[r][c] != "1":
                return
            grid[r][c] = 'x'
            if r+1 < rows:
                dfs(r+1, c)
            if r-1 >= 0:
                dfs(r-1, c)
            if c +1 < cols:
                dfs(r, c+1)
            if c-1 >=0:
                dfs(r, c-1)
        count = 0
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1":
                    count+=1
                    dfs(r, c)
        return count