# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#
# 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
#
#
# @param num int整型一维数组
# @return TreeNode类
#
class Solution:
    def sortedArrayToBST(self , num: List[int]) -> TreeNode:
        # write code here
        def helper(nums):
            if len(nums)==0:
                return None
            elif len(nums)==1:
                return TreeNode(nums[0])
            else:
                mid = int(len(nums)/2)
                node = TreeNode(nums[mid])
                node.left = helper(nums[0:mid])
                node.right = helper(nums[mid+1:-1])
                return node
        return helper(num)