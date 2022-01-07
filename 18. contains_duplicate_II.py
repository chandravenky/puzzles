
def contains_duplicate(input_array, k):

  map_dict = {}

  for index, value in enumerate(input_array):

    if value in map_dict:
      
      if index - map_dict[value] <=k:

        return True
      
      map_dict[value] = index
    
    else:
      map_dict[value] = index

  return False
