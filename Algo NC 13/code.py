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
    def maxDepth(self , root: TreeNode) -> int:
        # write code here
        def helper(root):
            if not root:
                return 0
            if root.left:
                if root.right:
                    return max(helper(root.left), helper(root.right))+1
                else:
                    return helper(root.left)+1
            else:
                if root.right:
                    return helper(root.right)+1
                else:
                    return 1
        return helper(root)