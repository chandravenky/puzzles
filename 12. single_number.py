#Solution1
def single_number(input_array):

  unique_track = {}

  for i in range(0,len(input_array)):
  

    if input_array[i] in list(unique_track.keys()):

      del unique_track[input_array[i]]
    
    else:
      unique_track[input_array[i]] = 1

  return list(unique_track.keys())[0]

#Solution 2
def single_number_2(input_array):

  res = input_array[0]

  for i in range(1, len(input_array)):

    #print(res, bin(res), input_array[i], bin(input_array[i]))

    res ^= input_array[i] #bitwise XOR

    #print("result", res, bin(res))

  return res
