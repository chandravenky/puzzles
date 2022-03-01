#Problem 383

def ransom_note(ransomNote, magazine):

  magazine_store = {}
        
  for i in range(0, len(magazine)):
      
    if magazine[i] not in magazine_store:
      magazine_store[magazine[i]] = 1
        
    else:
      magazine_store[magazine[i]] = magazine_store[magazine[i]] + 1
        
  for i in range(0, len(ransomNote)):
      
    if ransomNote[i] not in magazine_store:
      return False
      
    else:
      magazine_store[ransomNote[i]] = magazine_store[ransomNote[i]] - 1
          
      if magazine_store[ransomNote[i]] == 0:
        del magazine_store[ransomNote[i]]
              
  return True
