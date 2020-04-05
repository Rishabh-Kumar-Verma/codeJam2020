output=str('')


def Complement(preserve_input):
    preserve_list=list(preserve_input)
    for i in range(0,len(preserve_input)):
        if preserve_list[i]=='0':
            preserve_list[i]='1'
        else:
            preserve_list[i]='0'
    return ''.join(preserve_list)


def operate(out):
    
    preserve_input=''
    previous=''
    r_counter=0
    c_counter=0
    rc_counter=0
    n_counter=0
    count=0
    querry=1

    t,b=map(int, input().split(' '))

    while t!=0:
        preserve_input=''
        previous=''
        out=''
        r_counter=0
        c_counter=0
        rc_counter=0
        n_counter=0
        count=0
        querry=1
        while querry!=150:
            if count%10==0 and count!=0:
                if len(previous)==0 and len(out)!=0:
                    preserve_input=out
                else:
                    if out[::-1] == previous:
                        r_counter=r_counter+1
                    if  Complement(out)==previous :
                        c_counter=c_counter+1
                    if Complement(out[::-1])==previous:
                        rc__counter=rc_counter+1
                    else:
                        n_counter=n_counter+1

                previous=out
                out='' 
                count=0
                with open('history.txt' ,'a') as f:
                    print((r_counter,c_counter,rc_counter,n_counter,(out,previous)),file=f)
            
            print(count+1)
            count=count+1 
            querry=querry+1   
            r=str(input())
            if(r=='N'):
                break
            else:
                out=out+(r) 

        with open('out.txt' ,'a') as f:
            print((r_counter,c_counter,rc_counter,n_counter),file=f)
        
        preserve_input=previous

        if(r_counter == max([r_counter,n_counter,c_counter,rc_counter])):
            print(preserve_input[::-1])
        if c_counter == max([r_counter,n_counter,c_counter,rc_counter]):
            preserve_list=list(preserve_input)
            for i in range(0,len(preserve_input)):
                if preserve_list[i]=='0':
                    preserve_list[i]='1'
                else:
                    preserve_list[i]='0'
            preserve_input=''.join(preserve_list)

            print(preserve_input)
        if n_counter==max([r_counter,n_counter,c_counter,rc_counter]):
            print(preserve_input)
        if  rc_counter==max([r_counter,n_counter,c_counter,rc_counter]):
            preserve_list=list(preserve_input)
            for i in range(0,len(preserve_input)):
                if preserve_list[i]=='0':
                    preserve_list[i]='1'
                else:
                    preserve_list[i]='0'
            
            preserve_input=''.join(preserve_list)
            
            print(preserve_input[::-1])


        if input()!='Y':
            break
        t=t-1


if "__main__"==__name__:
    operate(output)