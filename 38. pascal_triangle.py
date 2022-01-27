def pascal_triangle(n):

  result_list = [[1], [1,1], [1,2,1]]

  if n<3:
    return result_list[:n]

  for i in range(3, n):

    num_elements_in_pattern = (i)//2
    
    calculated_list = []

    for j in range(1, num_elements_in_pattern+1):

      calculated_list.append(result_list[-1][j] + result_list[-1][j-1])

    if i%2!=0:

      current_row_res = [1] + calculated_list + calculated_list[::-1] + [1]

    else:
      current_row_res = [1] + calculated_list + calculated_list[:len(calculated_list)-1][::-1] + [1]
    
    result_list.append(current_row_res)

  return result_list
