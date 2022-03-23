import copy
def combine(n, k):
  """
  :type n: int
  :type k: int
  :rtype: List[List[int]]
  """
  def backtrack(first, curr=[]):
    if len(curr)==k:
      output.append(copy.deepcopy(curr))
      return
    for j in range(first, n+1):
      curr.append(j)
      backtrack(j+1, curr)
      curr.pop()
  
  output = []
  backtrack(1)
    
  return output
