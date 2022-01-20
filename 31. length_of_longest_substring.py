# Solution1
def length_of_longest_sub(input_string):

  tracker = {}
  first_slider=0
  second_slider=0
  longest_length=0

  for i in range(0, len(input_string)):
    
    second_slider =i +1

    if input_string[i] not in tracker:
      
      tracker[input_string[i]]=i

      if second_slider - first_slider > longest_length:

        longest_length = second_slider - first_slider

    else:

      first_slider = max(tracker[input_string[i]] + 1, first_slider)

      tracker[input_string[i]]  = i
      if second_slider - first_slider > longest_length:

        longest_length = second_slider - first_slider    

  return longest_length

#Tests
def length_of_longest_sub_test():

  input_string1 = "bbbbb"
  input_string2 = "abcabcbb"
  input_string3 = "pwwkew"
  input_string4 = " "
  input_string5 = "   "
  input_string6 = ""
  input_string7 = ""
  input_string8 = "aab"
  input_string9 = "dvdf"
  input_string10 = "ckilbkd"
  input_string11 = "ckilbkdp"
  input_string12 = "abba"
  
  expected_output1 = 1
  expected_output2 = 3
  expected_output3 = 3
  expected_output4 = 1
  expected_output5 = 1
  expected_output6 = 0
  expected_output7 = 1
  expected_output8 = 2
  expected_output9 = 3
  expected_output10 =5
  expected_output11 =6
  expected_output12 = 2


  return ( expected_output1 == length_of_longest_sub(input_string1), expected_output2 == length_of_longest_sub(input_string2), expected_output3 == length_of_longest_sub(input_string3), expected_output4 == length_of_longest_sub(input_string4), expected_output5 == length_of_longest_sub(input_string5), expected_output6 == length_of_longest_sub(input_string6), expected_output7 == length_of_longest_sub(input_string7), expected_output8 == length_of_longest_sub(input_string8), expected_output9 == length_of_longest_sub(input_string9), expected_output10 == length_of_longest_sub(input_string10), expected_output11 == length_of_longest_sub(input_string11), expected_output12 == length_of_longest_sub(input_string12) )

print(length_of_longest_sub_test())

#Leetcode
class Solution(object):
  def lengthOfLongestSubstring(self, input_string):
    """
    :type s: str
    :rtype: int
    """
    tracker = {}
    first_slider=0
    second_slider=0
    longest_length=0

    if input_string =="":
      return 0

    if len(input_string.strip()) == 0:
      return 1

    if len(input_string) ==1:
      return 1

    for i in range(0, len(input_string)):

      second_slider =i +1

      if input_string[i] not in tracker:

        tracker[input_string[i]]=i

        if second_slider - first_slider > longest_length:

          longest_length = second_slider - first_slider

      else:

        first_slider = max(tracker[input_string[i]] + 1, first_slider)

        tracker[input_string[i]]  = i

        if second_slider - first_slider > longest_length:

          longest_length = second_slider - first_slider    

    return longest_length




