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


def combine_test():

  input_n1 = 4
  input_n2 = 4

  input_k1 = 2
  input_k2 = 3

  expected_output1 = [[1,2],[1,3],[1,4],[2,3],[2,4],[3,4]]
  expected_output2 = [[1,2,3],[1,2,4],[1,3,4],[2,3,4]]

  result_tuple = ( expected_output1 == combine(input_n1, input_k1), expected_output2 == combine(input_n2, input_k2) )

  return result_tuple == ( True, True )

print(combine_test())
