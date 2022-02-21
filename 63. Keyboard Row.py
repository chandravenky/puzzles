#Problem 500



def find_words(words):

  row1 = list("qwertyuiop")
  row2 = list("asdfghjkl")
  row3 = list("zxcvbnm")

  result = []

  for i in range(0, len(words)):

    count = 0
    if len(set(words[i]).intersection(row1))>0:
      count = count+1

    if len(set(words[i]).intersection(row2))>0:
      count = count+1

    if len(set(words[i]).intersection(row3))>0:
      count = count+1

    if count == 1:
      result.append(words[i])
  
  return result
  
#Tests
def find_words_test():

  input_words1 = ["Hello","Alaska","Dad","Peace"]
  input_words2 = ["omk"]
  input_words3 = ["adsdf","sfd"]

  expected_output1 = ["Alaska","Dad"]
  expected_output2 = []
  expected_output3 = ["adsdf","sfd"]

  return ( expected_output1 == find_words(input_words1), expected_output2 == find_words(input_words2), expected_output3 == find_words(input_words3) )

print(find_words_test())

#Submit
class Solution(object):
    def validPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        pointer1 = 0
        pointer2 = len(s) - 1
        
        while pointer1 < pointer2:
            if s[pointer1] != s[pointer2]:
                
                string1 = s[pointer1:pointer2]
                string2 = s[pointer1+1:pointer2+1]
                
                if string1 == string1[::-1] or string2 == string2[::-1]:
                    return True
                else:
                    return False
            
            pointer1 = pointer1 + 1
            pointer2 = pointer2 - 1
            
        return True

