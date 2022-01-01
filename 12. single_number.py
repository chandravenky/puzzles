#Solution1
def single_number(input_array):

  unique_track = {}

  for i in range(0,len(input_array)):
  

    if input_array[i] in list(unique_track.keys()):

      del unique_track[input_array[i]]
    
    else:
      unique_track[input_array[i]] = 1

  return list(unique_track.keys())[0]
