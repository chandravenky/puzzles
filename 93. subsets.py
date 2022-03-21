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
