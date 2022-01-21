
#without dpp
def longest_palindrome(input_string):

  result= ''
  longest_length = 0

  for i in range(0, len(input_string)):
   
    #Odd palindromes
    left, right = i, i
    
    while left>=0 and right<len(input_string) and input_string[left]== input_string[right]:
      if right-left +1>longest_length:
        result = input_string[left: right+1]
        longest_length = right-left +1

      left = left -1
      right = right+1

    #Even checks
    left, right = i,i + 1
    while left>=0 and right<len(input_string) and input_string[left] == input_string[right]:
      if right-left +1>longest_length:
        result = input_string[left: right+1]
        longest_length = right-left +1

      left = left -1
      right = right+1


  return result

#With dp - not a good solution
def longest_palindrome2(s):

  dp = [[False]*len(s) for i in range(0, len(s))]

  max_pal = s[0]

  #fill diagonals with 1s
  for i in range(0, len(s)):
    dp[i][i] = True

  for i in reversed(range(len(s))):
      for j in reversed(range(i+1, len(s))):
        if s[i] == s[j]:
          if j-i==1 or dp[i+1][j-1]== True:
            dp[i][j]=True

            if len(s[i:j+1]) >= len(max_pal):
              max_pal = s[i:j+1]

  return max_pal

#Tests
def longest_palindrome_test():

  input_string1 = "babad"
  input_string2 = "cbbd"
  input_string3 = "cbbdc"
  input_string4 = "cabbdxc"
  input_string5 = "xabay"
  input_string6 = "aaaa"

  expected_output1a = "bab"
  expected_output1b = "aba"
  expected_output2 = "bb"
  expected_output3 = "bb"
  expected_output4 = "bb"
  expected_output5 = "aba"
  expected_output6 = "aaaa"

  return ( expected_output1a == longest_palindrome(input_string1), expected_output2 == longest_palindrome(input_string2), expected_output3 == longest_palindrome(input_string3), expected_output4 == longest_palindrome(input_string4), expected_output5 == longest_palindrome(input_string5),
  expected_output6 == longest_palindrome(input_string6), 

  expected_output1b == longest_palindrome2(input_string1), expected_output2 == longest_palindrome2(input_string2), expected_output3 == longest_palindrome2(input_string3), expected_output4 == longest_palindrome2(input_string4), expected_output5 == longest_palindrome2(input_string5),
  expected_output6 == longest_palindrome2(input_string6) )

print(longest_palindrome_test())

#Leetcode
#Without dp
class Solution(object):
    def longestPalindrome(self, input_string):
        """
        :type s: str
        :rtype: str
        """

        result= ''
        longest_length = 0

        for i in range(0, len(input_string)):

        #Odd palindromes
            left, right = i, i

            while left>=0 and right<len(input_string) and input_string[left]== input_string[right]:

                if right-left +1>longest_length:
                    result = input_string[left: right+1]
                    longest_length = right-left +1

                left = left -1
                right = right+1

            #Even checks
            left, right = i,i + 1
            while left>=0 and right<len(input_string) and input_string[left] == input_string[right]:
                if right-left +1>longest_length:
                    result = input_string[left: right+1]
                    longest_length = right-left +1

                left = left -1
                right = right+1


        return result

#with dp
class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        dp = [[False]*len(s) for i in range(0, len(s))]

        max_pal = s[0]

        #fill diagonals with 1s
        for i in range(0, len(s)):
            dp[i][i] = True

        for i in reversed(range(len(s))):
            for j in reversed(range(i+1, len(s))):
                if s[i] == s[j]:
                    if j-i==1 or dp[i+1][j-1]== True:
                        dp[i][j]==True

                        if len(max_pal) < len(s[i:j+1]):
                            max_pal = s[i:j+1]

        return max_pal
