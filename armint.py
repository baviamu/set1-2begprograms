b,dc=map(int,input().split())
for n in range(b+1,dc):
  ch=n
  fndi=0
  while (n>0):
    a=n%10
    fndi=fndi+(a**3)
    n=n//10
    if(fndi==ch):
      print(fndi,end=" ")
