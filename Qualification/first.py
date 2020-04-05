
output=[]
count=1  

if "__main__"==__name__:
    
    sample= int(input())

    while(sample):

        nxm=int(input())

        a = [[0]*nxm]*nxm
        n_row=0
        n_col=0
        d_count=0
 
        for i in range(0,nxm):
                a[i]=list(map(int,input().split(' ')))
                d_count=d_count+a[i][i]



        for row in a:
            uniq = [item for item in row if row.count(item) > 1]
            if len(uniq)>0:
                n_row=n_row+1

        a=[[row[i] for row in a] for i in range(len(a[0]))]

        for col in a:
            uniq = [item for item in col if col.count(item) > 1]
            if len(uniq)>0:
                n_col=n_col+1
        
        output.append('Case #' + str(count) +': '+str(d_count)+' '+ str(n_row) +' '+str(n_col))

        count=count+1
        sample=sample-1

for exe in output:
    print(exe)


