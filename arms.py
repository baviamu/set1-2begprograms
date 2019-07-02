bee=int(input())
length=le(str(bee))
su=0
tem=A
while(tem!=0) and (A<=100000):
   su=su+((tem%10)**length)
   tem=tem//10
if su==A:
    print("yes")
else:
    print("no")
