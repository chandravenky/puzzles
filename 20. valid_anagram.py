#Solution1
def is_anagram(s, t):

  s_count = {}

  for letter in s:

    if letter in s_count:
      s_count[letter] = s_count[letter] + 1

    else:
      s_count[letter] = 1


  for letter in t:

    if letter in s_count:
      s_count[letter] = s_count[letter] -1

      if s_count[letter] == 0:
        del s_count[letter]

    else:
      return False

  if s_count:
    return False

  return True

# Tests
def is_anagram_test():

  input_case1 = ('anagram', 'nagaram')
  input_case2 = ('rat', 'car')
  input_case3 = ('ab', 'a')

  return ( is_anagram(input_case1[0], input_case1[1]) == True, is_anagram(input_case2[0], input_case2[1]) == False, is_anagram(input_case3[0], input_case3[1]) == False)

print(is_anagram_test())

#Leetcode
class Solution(object):
  def isAnagram(self, s, t):
    """
    :type s: str
    :type t: str
    :rtype: bool
    """
    s_count = {}
    
    if len(s) != len(t):
      return False

    for letter in s:

      if letter in s_count:
        s_count[letter] = s_count[letter] + 1

      else:
        s_count[letter] = 1

    for letter in t:

      if letter in s_count:
        s_count[letter] = s_count[letter] -1

        if s_count[letter] == 0:
          del s_count[letter]

        else:
          return False
    if s_count:
      return False

    return True

