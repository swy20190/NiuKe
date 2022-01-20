#
# 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
#
# 递增路径的最大长度
# @param matrix int整型二维数组 描述矩阵的每个数
# @return int整型
#
class Solution:
    def solve(self , matrix: List[List[int]]) -> int:
        # write code here
        self.map = matrix
        self.n = len(matrix)
        self.m = len(matrix[0])
        def dfs(i, j):
            if i<0 or i>=self.n or j<0 or j>=self.m:
                return 0
            ret = 1
            if i>0 and self.map[i-1][j]>self.map[i][j]:
                ret = max(ret, 1+dfs(i-1, j))
            if i<self.n-1 and self.map[i+1][j]>self.map[i][j]:
                ret = max(ret, 1+dfs(i+1, j))
            if j>0 and self.map[i][j-1]>self.map[i][j]:
                ret = max(ret, 1+dfs(i, j-1))
            if j<self.m-1 and self.map[i][j+1]>self.map[i][j]:
                ret = max(ret, 1+dfs(i, j+1))
            return ret
        answer = 0
        for i in range(self.n):
            for j in range(self.m):
                answer = max(answer, dfs(i,j))
        return answer