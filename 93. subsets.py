def subsets(nums):
  """
  :type nums: List[int]
  :rtype: List[List[int]]
  """
  def backtrack(first=0, curr = []):
    
    if len(curr)==k:
      output.append(curr[:])
      return
    for i in range(first, n):
      curr.append(nums[i])
      backtrack(i+1, curr)
      #keep carrying over pops
      curr.pop()
        
  output = []
  n = len(nums)
  
  #each len of the subset
  for k in range(0, n+1):
      backtrack()
      
  return output

def subsets_test():

  input_nums1 = [1,2,3]
  input_nums2 = [0]

  expected_output1 = [[],[1],[2],[3],[1,2],[1,3],[2,3],[1,2,3]]
  expected_output2 = [[],[0]]

  return ( expected_output1 == subsets(input_nums1), expected_output2 == subsets(input_nums2) )

print(subsets_test())

#Solution
class Solution(object):
  def subsets(self, nums):
    """
    :type nums: List[int]
    :rtype: List[List[int]]
    """
    def backtrack(first=0, curr = []):
      
      if len(curr)==k:
        output.append(curr[:])
        return
      for i in range(first, n):
        curr.append(nums[i])
        backtrack(i+1, curr)
        #keep carrying over pops
        curr.pop()
            
    output = []
    n = len(nums)
    
    #each len of the subset
    for k in range(0, n+1):
      backtrack()
        
    return output
      
