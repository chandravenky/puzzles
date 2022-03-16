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
