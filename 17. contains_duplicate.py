
def contains_duplicate(input_array):

  map_dict = {}

  for i in range(0, len(input_array)):

    if input_array[i] in map_dict:
      return True
    
    else:
      map_dict[input_array[i]] = 1

  return False
