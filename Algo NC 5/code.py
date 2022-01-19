# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#
# 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
#
#
# @param root TreeNode类
# @return int整型
#

class Solution:

    def sumNumbers(self, root: TreeNode) -> int:
        # write code here
        def dfs(root, curr_sum):
            if not root:
                return 0
            else:
                new_sum = curr_sum * 10 + root.val
                if (not root.left) and (not root.right):
                    return new_sum
                else:
                    return dfs(root.left, new_sum) + dfs(root.right, new_sum)

        return dfs(root, 0)