#Problem 46

def permute(nums):
    
    res = []
    perm = []
  
    def backtrack(i):
      if i == len(nums):
        res.append(perm.copy())
        return
        
      for num in nums:
        if num not in perm:
          
          perm.append(num)
          backtrack(i + 1)
          perm.pop()
          
    backtrack(0)
  
    return res

def permute_test():

  input_nums1 = [1,2,3]
  input_nums2 = [0,1]
  input_nums3 = [1]

  expected_output1 = [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
  expected_output2 = [[0,1],[1,0]]
  expected_output3 = [[1]]

  return ( expected_output1 == permute(input_nums1), expected_output2 == permute(input_nums2), expected_output3 == permute(input_nums3) )

print(permute_test())

#Submission
import copy
class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        
        res = []
        perm = []

        def backtrack(i):
            if i == len(nums):
                res.append(copy.deepcopy(perm))
                return

            for num in nums:
                if num not in perm:

                    perm.append(num)
                    backtrack(i + 1)
                    perm.pop()

        backtrack(0)

        return res
                
