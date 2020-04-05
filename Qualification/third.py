
output=[]
count=1  

if "__main__"==__name__:
    
    sample= int(input())

    while(sample):

        nxm=int(input())

        a = [[0]*2]*nxm
        st=''
        c_working,j_working=1,1
        c_temp,j_temp=[],[]
 
        for i in range(0,nxm):
                a[i]=list(map(int,input().split(' ')))


        for row in a:
            if len(c_temp)==0:
                st=st+str('J')
                c_temp.append(row)
                c_working=0
            else:
                for i in c_temp:
                    if row[1] <= i[0]  or row[0] >= i[1]:
                        c_working=0
                    else:
                        c_working=1
                        break
                if c_working==0:
                    st=st+str('J')
                    c_temp.append(row)

            if c_working:
                if len(j_temp)==0:
                    st=st+str('C')
                    j_temp.append(row)
                    j_working=0
                else:
                    for i in j_temp:
                        if row[1] <= i[0]  or row[0] >= i[1]:
                            j_working=0
                        else:
                            j_working=1
                            break
                    if j_working==0:
                        st=st+str('C')
                        j_temp.append(row)
            
            #print(j_temp,c_temp)
            if j_working and c_working:
                st=str('IMPOSSIBLE')
                break         
    

        
        output.append('Case #' + str(count) +': '+st)

        count=count+1
        sample=sample-1

for exe in output:
    print(exe)


