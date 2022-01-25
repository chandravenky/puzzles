def climb_stairs(n):

  ways=[0, 1,2,3]

  if n<=3:
    return n

  for i in range(3, n):

    ways.append(ways[-1] + ways[-2])

  return ways[-1]
