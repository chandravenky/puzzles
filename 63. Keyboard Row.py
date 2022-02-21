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
