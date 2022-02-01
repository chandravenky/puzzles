# Solution
def count_points(input_string):

  ring_tracker = {}

  for i in range(0, len(input_string),2):

    ring_color = input_string[i]
    rod_number = input_string[i+1]

    if rod_number not in ring_tracker:
      ring_tracker[rod_number] = [ring_color]

    else:
      
      if ring_color not in ring_tracker[rod_number]:

        ring_tracker[rod_number].append(ring_color )

  #filter for values with length ==3
  filtered_ring_tracker = { key:value for key, value in ring_tracker.items() if len(value)==3}

  return len(filtered_ring_tracker.keys())
