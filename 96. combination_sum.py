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
