res=int(input())
bc=list(map(int,input().split()[:res]))
bc.sort()
for l in bc:
	print(l,end=" ")
