class Solution(object):
    def numJewelsInStones(self, jewels, stones):
        """
        :type jewels: str
        :type stones: str
        :rtype: int
        """
        jewel_store = {}
        
        for jewel in jewels:
            if jewel in jewel_store:
                pass
            else:
                jewel_store[jewel] = 1
        
        count = 0
        
        for stone in stones:
            
            if stone in jewel_store:
                count = count + 1
        
        return count
