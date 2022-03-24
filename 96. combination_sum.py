import copy
def combination_sum(candidates, target):

  def backtrack(first, curr=[]):
    if sum(curr) == target:
      if curr not in output:
        output.append(copy.deepcopy(curr))
      return
    if sum(curr) >target:
      return
    for i in range(first, n):
      curr.append(candidates[first])
      #print(curr)
      backtrack(i,curr)
      curr.pop()

  output = []
  n = len(candidates)
  for i in range(0, n):
    backtrack(i,[])

  return output



def combination_sum_test():

  input_candidates1 = [2,3,6,7]
  input_candidates2 = [2,3,5]
  input_candidates3 = [2]

  input_target1 = 7
  input_target2 = 8
  input_target3 = 1

  expected_output1 = [[2,2,3],[7]]
  expected_output2 = [[2,2,2,2],[2,3,3],[3,5]]
  expected_output3 = []

  return ( expected_output1 == combination_sum(input_candidates1, input_target1), expected_output2 == combination_sum(input_candidates2, input_target2), expected_output3 == combination_sum(input_candidates3, input_target3) )
