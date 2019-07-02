bbc,abc=map(int,input().split())
for c in range(bbc+1,abc,1):
  if(c%2!=0):
    print(c, end=' ')
