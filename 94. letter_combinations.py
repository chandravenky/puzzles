#Backtracking using strings
class Solution(object):
    def letterCombinations(self, digit):
        """
        :type digits: str
        :rtype: List[str]
        """
        map_dict = {    '2': list("abc"),
                       '3': list("def"),
                       '4': list("ghi"),
                       '5': list("jkl"),
                       '6': list("mno"),
                       '7': list("pqrs"),
                       '8': list("tuv"),
                       '9': list("wxyz")
               }
      


        def backtrack(i, curr):
            if len(curr) == n:
                output.append(curr)
                return

            for char in map_dict[digit[i]]:
                backtrack(i+1, curr + char)


        output =[]            
        n = len(digit)

        if digit:
            backtrack(0, '')
            
        return output
