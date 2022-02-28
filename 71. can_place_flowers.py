#Problem 605

def can_place_mismatch(flowerbed, n):

  i = 0
  
  while i<len(flowerbed):
    
    if flowerbed[i] == 0:
      
      if i == len(flowerbed)-1:
        n=n-1
        break
      elif flowerbed[i+1] == 0:
        n = n-1
        i= i+2
      else:
        i=i+3
    
    else:
      i = i+2
          
  return n<=0
