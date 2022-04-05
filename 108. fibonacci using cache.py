class Solution(object):
    
    cache = {0: 0, 1: 1}
    
    def fib(self, n):
        """
        :type n: int
        :rtype: int
        """
        
        if n in self.cache:
            return self.cache[n]
        
        else:
            self.cache[n] = self.fib(n-1) + self.fib(n-2)
            
            return self.cache[n]
