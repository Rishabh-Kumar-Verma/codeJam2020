from itertools import combinations_with_replacement

output=[]
result=str('')
mat=[]
count=1
index=0
  
def findQuad(lst, K): 
    return [list(pair) for pair in combinations_with_replacement(lst, len(lst)) if sum(pair) == K] 

def print_grid(arr): 
    for i in range(len(arr)): 
        for j in range(len(arr)): 
            print(arr[i][j], end=' ') 
        print() 
  
           
def find_empty_location(arr,l): 
    for row in range(index): 
        for col in range(index): 
            if(arr[row][col]==0): 
                l[0]=row 
                l[1]=col 
                return True
    return False
  

def used_in_row(arr,row,num): 
    for i in range(index): 
        if(arr[row][i] == num): 
            return True
    return False

def used_in_col(arr,col,num): 
    for i in range(index): 
        if(arr[i][col] == num): 
            return True
    return False
    

def check_location_is_safe(arr,row,col,num): 
    return not used_in_row(arr,row,num) and not used_in_col(arr,col,num)
 
def solve_sudoku(arr): 
        
    l=[0,0] 
          
    if(not find_empty_location(arr,l)): 
        return True
      
    row=l[0] 
    col=l[1] 
      
    for num in range(1,index+1): 
        if(check_location_is_safe(arr,row,col,num)): 

            arr[row][col]=num 
  
            if(solve_sudoku(arr)): 
                return True
  
            arr[row][col] = 0
                     
    return False 


if "__main__"==__name__:
    
    sample= int(input())

    while(sample):

        [nxm,d_count]=map(int,input().split(' '))

        combi=[item for item in range(1,nxm+1)]
        combi=findQuad(combi,d_count)
        
        index=nxm
        grid=[[0 for x in range(index)]for y in range(index)]

        if len(combi)!=0:
            for i in combi:
                for j in range(0,len(i)):
                    grid[j][j]=i[j]
                if(solve_sudoku(grid)):
                    st='POSSIBLE'
                    break
                else:
                    st='IMPOSSIBLE'
        else:
            st='IMPOSSIBLE'
            grid=[]

        output.append(['Case #' + str(count) +': '+st+' ',grid,st])

        count=count+1
        sample=sample-1

for exe in output:
    print(exe[0])
    if(exe[2]=='POSSIBLE'):
        print_grid(exe[1])


