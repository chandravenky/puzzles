#Problem 1232

class Solution(object):
    def checkStraightLine(self, coordinates):
        """
        :type coordinates: List[List[int]]
        :rtype: bool
        """
        
        if len(coordinates)<=2:
            return True
        
        if coordinates[1][0] - coordinates[0][0] == 0:
            
            for i in range(1, len(coordinates)):
                if coordinates[i][0] !=coordinates[0][0]:
                    return False
                
            return True
            
        slope = (coordinates[1][1] - coordinates[0][1])/ (coordinates[1][0] - coordinates[0][0])
        
        for i in range(1, len(coordinates)-1):
            
            if coordinates[i+1][0] - coordinates[i][0]==0:
                return False
            
            current_slope = (coordinates[i+1][1] - coordinates[i][1])/ (coordinates[i+1][0] - coordinates[i][0])
            
            if current_slope != slope:
                return False
            
        return True
