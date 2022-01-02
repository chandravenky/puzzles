# #Solution - Best
def excel_sheet_column_num(input_col_num):

  map_dict = '0ABCDEFGHIJKLMNOPQRSTUVWXYZ'
  result = ''


  if input_col_num <=26:
      return map_dict[input_col_num]

  else:

      while input_col_num>0:

          input_col_num, remainder = divmod(input_col_num,26)

          if remainder == 0:

              remainder = 26
              input_col_num = input_col_num -1
          result = map_dict[remainder] + result

  return result

#Less readable - uses original index
def excel_sheet_column_num_2(input_col_num):

  map_dict = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
  result = ''

  if input_col_num <=26:
    return map_dict[input_col_num-1]

  else:

    while input_col_num>0:

      input_col_num, remainder = divmod(input_col_num,26)
      
      if remainder == 0:

        remainder = 26
        input_col_num = input_col_num -1
      
      result = map_dict[remainder-1] + result

  return result
