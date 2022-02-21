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
