# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#
# 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
#
#
# @param pre int整型一维数组
# @param vin int整型一维数组
# @return TreeNode类
#
class Solution:
    def reConstructBinaryTree(self , pre: List[int], vin: List[int]) -> TreeNode:
        # write code here
        def helper(pre, vin):
            if len(pre)==0:
                return None
            node = TreeNode(pre[0])
            if len(pre)==1:
                return node
            idx = 0
            for i in range(len(vin)):
                if vin[i]==pre[0]:
                    idx = i
                    break
            node.left = helper(pre[1:idx+1], vin[0:idx])
            node.right = helper(pre[idx+1:], vin[idx+1:])
            return node
        return helper(pre, vin)