class Solution:
    def minCostClimbingStairs(self, cost):
        """
        :type cost: List[int]
        :rtype: int
        """
        '''
        recursive way : Time Limit Exceeded
        '''
        
        '''
        if len(cost)==1 or len(cost)==2 or len(cost)==3:
            return min(cost) if len(cost)!=3 else min(cost[0]+cost[2],cost[1])
        return min(self.minCostClimbingStairs(cost[0:len(cost)-2]) + cost[len(cost)-2],
                   self.minCostClimbingStairs(cost[0:len(cost)-1]) + cost[len(cost)-1])
        '''
        
        '''
        forward way
        '''
        if len(cost)<=2:
            return min(cost)
        prev_1, prev_2 = cost[1], cost[0]
        cost[1], cost[0] = 0, 0
        for i in range(2,len(cost)):
            res = min(prev_1 + cost[i-1], prev_2 + cost[i-2])
            prev_1, prev_2 = res, prev_1
        return min(prev_1 + cost[-1],prev_2 + cost[-2])
