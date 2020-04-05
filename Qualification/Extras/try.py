from itertools import combinations_with_replacement


output=[]
mat=[]
count=1
  
def findPairs(lst, K): 
    return [list(pair) for pair in combinations_with_replacement(lst, 3) if sum(pair) == K] 
      
# Driver code 
lst = [1,2,3] 
K = 6
print(findPairs(lst, K)) 