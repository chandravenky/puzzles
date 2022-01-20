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
