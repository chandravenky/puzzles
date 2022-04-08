#Not the best solution
class Solution(object):
    def heightChecker(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        
        heights_sorted = sorted(heights)
        
        count = 0
        
        for i in range(0, len(heights)):
            
            if heights[i]!=heights_sorted[i]:
                count = count+1
                
        return count
        
