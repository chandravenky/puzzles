# Solution
def backspace_compare(s,t):

  stack_a = []
  stack_b = []

  for i in range(0, len(s)):
    
    if s[i] == '#':

      if len(stack_a) ==0:
        pass
      else:
        stack_a.pop()

    else:
      stack_a.append(s[i])

  for j in range(0, len(t)):
    
    if t[j] == '#':
      
      if len(stack_b) ==0:
        pass
      else:
        stack_b.pop()

    else:
      stack_b.append(t[j])

  #string output of stack_a
  stack_a_string = ''.join(stack_a)

  #string output of stack_b
  stack_b_string = ''.join(stack_b)
  
  return stack_a_string == stack_b_string
