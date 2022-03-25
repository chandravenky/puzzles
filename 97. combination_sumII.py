import copy
class Solution(object):
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        #unique and sort
        candidates = sorted(candidates)
        
        def backtracking(first, curr=[]):
            if sum(curr) == target:
                if curr not in output:
                    output.append(copy.deepcopy(curr))
            if sum(curr)> target:
                return
            
            prev = -99999
            for i in range(first, n):
                if candidates[i] == prev:
                    continue
                curr.append(candidates[i])
                backtracking(i+1, curr)
                curr.pop()
                prev = candidates[i]
            
        output = []
        n = len(candidates)
        backtracking(0,[])
            
        return output
        
