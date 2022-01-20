#
# 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
#
#
# @param grid int整型二维数组
# @return int整型
#
class Solution:
    def maxAreaIsland(self , grid: List[List[int]]) -> int:
        # write code here
        self.map = grid
        self.n = len(grid)
        self.m = len(grid[0])
        def dfs(i, j):
            if i<0 or i>=self.n or j<0 or j>=self.m:
                return 0
            if self.map[i][j]==0:
                return 0
            else:
                self.map[i][j] = 0
                return 1+dfs(i-1, j)+dfs(i+1, j)+dfs(i, j-1)+dfs(i, j+1)
        answer = 0
        for i in range(self.n):
            for j in range(self.m):
                answer = max(answer, dfs(i, j))
        return answer