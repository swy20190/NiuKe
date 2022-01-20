#
# 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
#
#
# @param s string字符串
# @return string字符串一维数组
#
class Solution:
    def generatePermutation(self, s: str) -> List[str]:
        # write code here
        self.res = set()
        self.str = s

        def dfs(idx, curr_str):
            if idx > len(self.str):
                return
            else:
                self.res.add(curr_str)
                for i in range(idx, len(self.str)):
                    dfs(i + 1, curr_str + self.str[i])

        dfs(0, "")

        return list(self.res)