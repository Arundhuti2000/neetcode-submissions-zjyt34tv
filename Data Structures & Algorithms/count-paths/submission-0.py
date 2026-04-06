class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        my_grid=[]
        for i in range(m):
            my_grid.append([0]*n)
        for i in range(n):
            my_grid[0][i] = 1
        for j in range(m):
            my_grid[j][0] = 1
        
        for i in range(1,m):
            for j in range(1,n):
                my_grid[i][j]= my_grid[i-1][j]+ my_grid[i][j-1]

        return my_grid[m-1][n-1]