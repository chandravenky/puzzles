
def excel_sheet_col_num(input_col_name):

  input_col_name = input_col_name.lower()

  num = 0

  for i in range(0, len(input_col_name)):

    num = num + ((26** (len(input_col_name)-i-1))*(ord(input_col_name[i])-96))

  return num
