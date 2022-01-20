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
# @return int整型二维数组
#
class Solution:
    def levelOrder(self , root: TreeNode) -> List[List[int]]:
        # write code here
        self.res = []
        def solve(root, level):
            if not root:
                return
            if level==len(self.res):
                self.res.append([])
            self.res[level].append(root.val)
            solve(root.left, level+1)
            solve(root.right, level+1)
        solve(root, 0)
        return self.res