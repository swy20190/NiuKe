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
# @param sum int整型
# @return bool布尔型
#
class Solution:
    def hasPathSum(self , root: TreeNode, sum: int) -> bool:
        # write code here
        def dfs(root, s):
            if not root:
                return False
            if root.left:
                if root.right:
                    return dfs(root.left, s-root.val) or dfs(root.right, s-root.val)
                else:
                    return dfs(root.left, s-root.val)
            else:
                if root.right:
                    return dfs(root.right, s-root.val)
                else:
                    return s==root.val
        return dfs(root, sum)