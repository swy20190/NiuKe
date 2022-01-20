#
# 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
#
#
# @param n int整型
# @return string字符串一维数组
#
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        # write code here
        self.res = []

        def solve(left_n, right_n, curr_str):
            if left_n == 0:
                if right_n == 0:
                    self.res.append(curr_str)
                    return
                else:
                    solve(left_n, right_n - 1, curr_str + ")")
            else:
                if left_n == right_n:
                    solve(left_n - 1, right_n, curr_str + "(")
                else:
                    solve(left_n - 1, right_n, curr_str + "(")
                    solve(left_n, right_n - 1, curr_str + ")")

        solve(n, n, "")
        return self.res