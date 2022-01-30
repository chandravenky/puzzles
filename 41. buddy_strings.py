def buddy_strings(s, goal):
  """
  :type s: str
  :type goal: str
  :rtype: bool
  """
  if len(s) != len(goal):
    return False

  unmatch = {}
  match={}

  for i in range(0, len(s)):

    if s[i]!= goal[i]:
      unmatch[s[i]] = i

    else:
      match[s[i]] = 1 if s[i] not in match else match[s[i]] + 1

    if len(unmatch)>2:
      return False

  same_key = {key:value for key, value in match.items() if value>=2}
  
  if len(unmatch)==1:
    return False
  
  if len(unmatch)<2 and len(same_key)==0:
    return False

  elif len(unmatch)==0 and len(same_key)>0:
    return True

  else:

    #replace in s
    letters = [letter for letter in unmatch.keys()]
    indices = [index for index in unmatch.values()]

    #swap
    s_new = list(s)
    s_new[indices[0]] = letters[1]
    s_new[indices[1]] = letters[0]
    s_new = ''.join(s_new)

    if s_new == goal:
      return True

    return False

#9:55
#10:14

def buddy_strings_test():

  expected_output1 = True
  expected_output2 = False
  expected_output3 = True
  expected_output4 = True
  expected_output5 = False

  result_tuple = ( expected_output1 == buddy_strings("ab", "ba"), expected_output2 == buddy_strings("ab", "ab"), expected_output3 == buddy_strings("aa", "aa"), expected_output4 == buddy_strings("banana", "banana"), expected_output5 == buddy_strings("abac", "abad") )

  return result_tuple

print(buddy_strings_test())
