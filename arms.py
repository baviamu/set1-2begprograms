bee=int(input())
length=len(str(bee))
su=0
tem=bee
while(tem!=0) and (bee<=100000):
   su=su+((tem%10)**length)
   tem=tem//10
if su==bee:
    print("yes")
else:
    print("no")
