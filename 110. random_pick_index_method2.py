#This solution has O(n) time but O(1) pick

class Solution(object):

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.nums = nums

    def pick(self, target):
        """
        :type target: int
        :rtype: int
        """
        #Initialize with 0
        cnt = 0
        idx = 0
        
        #Loop through all items
        for index, value in enumerate(self.nums):
            
            #If value is not equal to target, continue to next item
            if value != target:
                continue
            
            #If value is equal, then check if the count if 0
            if cnt == 0:
                idx = index
                cnt = 1
                
            else:
                rand_int = random.randint(0, cnt) #Generate a random number between 0 to cnt all inclusive
                if (rand_int == cnt):#If random number is equal to count, update the return idx value
                    idx = index
                cnt += 1 #Increase the count everytime index matches the target

        return idx
                
        


# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.pick(target)
