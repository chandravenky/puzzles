#Problem 657

def judge_circle(moves):

  shift = {
          'U': [1,0],
          'D': [-1,0],
          'L': [0,-1],
          'R': [0,1]
          }
  init = [0,0]
    
  moves_list = list(moves)
    
  for move in moves_list:
        
    init = [init[0] + shift[move][0], init[1] + shift[move][1]]
        
  return init == [0,0]

#Add tests
def judge_circle_test():

  input_moves1 = "UD"
  input_moves2 = "LL"

  expected_output1 = True
  expected_output2 = False

  return ( expected_output1 == judge_circle(input_moves1), expected_output2 == judge_circle(input_moves2) )

print(judge_circle_test())
