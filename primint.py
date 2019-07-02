bb,vd=map(int,input().split())
for e in range(bb+1,vd,1):
    if(e>1):
        for f in range(2,e):
            if(e%f==0):
                break
        else:
            print(e,end=" ")
