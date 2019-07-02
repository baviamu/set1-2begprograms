bbc=int(input())
if (bbc<=1000):
   for i in range(2,bbc):
       if(bbc%i==0):
         print("no")
         break
   else:
       print("yes")
else:
    print("no")
