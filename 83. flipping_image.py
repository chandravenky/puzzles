#Problem 832

#Final submission
class Solution(object):
    def flipAndInvertImage(self, image):
        """
        :type image: List[List[int]]
        :rtype: List[List[int]]
        """
        #horizontal flip
        
        for unit in image:
            
            for i in range(0, int(len(unit)//2)):
                holding_val = unit[i] 
                unit[i] = unit[len(unit)-1-i]
                unit[len(unit)-1-i] = holding_val
                
        #invert
        for unit in image:
            
            for i in range(0, len(unit)):
                unit[i] = 0 if unit[i]==1 else 1
                
        return image
                
        
