#This solution has O(n) memory but O(1) pick

class Solution(object):

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.store = {}
        for index, value in enumerate(nums):
            if value in self.store:
                self.store[value].append(index)
            else:
                self.store[value] = [index]

    def pick(self, target):
        """
        :type target: int
        :rtype: int
        """
        return random.choice(self.store[target])
                
        


# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.pick(target)
