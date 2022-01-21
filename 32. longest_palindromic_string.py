
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
