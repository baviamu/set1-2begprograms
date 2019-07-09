bud=input()
cnt=0
for p in range(0,len(bud)):
    if(bud[p].isdigit() or bud[p].isalpha() or bud[p]==' '):
        continue
    else:
        cnt=cnt+1
print(cnt)
