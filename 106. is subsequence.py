class Solution(object):
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        
        if not s:
            return True
        
        s = list(s)
        t = list(t)
        s_pointer = 0
        t_pointer = 0
        
        while t_pointer<len(t) and s_pointer<len(s):
            
            if t[t_pointer] == s[s_pointer]:
                s_pointer = s_pointer + 1
                
            t_pointer = t_pointer + 1
            
        if s_pointer == len(s):
            return True
        return False
        
