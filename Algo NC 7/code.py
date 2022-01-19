#
# 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
#
#
# @param prices int整型一维数组
# @return int整型
#
class Solution:
    def maxProfit(self , prices: List[int]) -> int:
        # write code here
        answer = 0
        curr_min = prices[0]
        for i in range(1, len(prices)):
            answer = max(answer, prices[i]-curr_min)
            curr_min = min(curr_min, prices[i])
        return answer