
output=[]
count=1  

if "__main__"==__name__:
    
    sample= int(input())

    while(sample):
        st=str(input())

        result=''
        repeat,loops=1,0

        for i in range(0,len(st)):
            repeat=repeat+int(st[i])
            result=result+("("*int(st[i]) + st[i] + ")"*int(st[i]))
            
        for j in range(0,int(repeat/2)):
            result=result.replace(')(','')
    
        output.append('Case #' + str(count) +': '+ result)

        count=count+1
        sample=sample-1

for exe in output:
    print(exe)


