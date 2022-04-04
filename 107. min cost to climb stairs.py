class Solution(object):
    def minCostClimbingStairs(self, cost):
        """
        :type cost: List[int]
        :rtype: int
        """
        cost.append(0)
        
        dp = [cost[0], min(cost[0] + cost[1], cost[1])]
        
        for i in range(2, len(cost)):
            
            dp.append(min(dp[-1] + cost[i], dp[-2] + cost[i]))
            
        
        return dp[-1]
