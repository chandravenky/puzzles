#Problem 22
def generate_parenthesis(n):
    """
    :type n: int
    :rtype: List[str]
    """
    stack = []
    result = []
    
    def backtrack(open_n, closed_n):
      if open_n == closed_n == n:
        result.append(''.join(stack))
          
      if open_n<n:
        stack.append("(")
        backtrack(open_n+1, closed_n)
        stack.pop()
          
      if closed_n < open_n:
        stack.append(")")
        backtrack(open_n, closed_n+1)
        stack.pop()
    
    backtrack(0,0)
    
    return result

def generate_parenthesis_test():

  input_n1 = 3
  input_n2 = 1

  expected_output1 = ["((()))","(()())","(())()","()(())","()()()"]
  expected_output2 = ["()"]

  return ( expected_output1 == generate_parenthesis(input_n1), expected_output2 == generate_parenthesis(input_n2) )

print(generate_parenthesis_test())

#Submit
class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        stack = []
        result = []
        
        def backtrack(open_n, closed_n):
            if open_n == closed_n == n:
                result.append(''.join(stack))
                
            if open_n<n:
                stack.append("(")
                backtrack(open_n+1, closed_n)
                stack.pop()
                
            if closed_n < open_n:
                stack.append(")")
                backtrack(open_n, closed_n+1)
                stack.pop()
        
        backtrack(0,0)
        
        return result
        
