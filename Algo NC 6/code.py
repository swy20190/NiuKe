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
    def maxPathSum(self , root: TreeNode) -> int:
        # write code herejavascript:void(0);
        def dfs(root):
            if not root:
                return 0, 0
            else:
                if (not root.left)and(not root.right):
                    return root.val, root.val
                elif root.left and root.right:
                    left_max, left_half = dfs(root.left)
                    right_max, right_half = dfs(root.right)
                    curr_max = max(left_max, right_max, left_half+root.val, right_half+root.val, left_half+right_half+root.val, root.val)
                    curr_half = max(max(left_half, right_half)+root.val, root.val)
                    return curr_max, curr_half
                elif root.left and not root.right:
                    left_max, left_half = dfs(root.left)
                    curr_max = max(left_max, left_half+root.val, root.val)
                    curr_half = max(left_half+root.val, root.val)
                    return curr_max, curr_half
                else:
                    right_max, right_half = dfs(root.right)
                    curr_max = max(right_max, right_half+root.val, root.val)
                    curr_half = max(right_half+root.val, root.val)
                    return curr_max, curr_half
        answer, half = dfs(root)
        return answer