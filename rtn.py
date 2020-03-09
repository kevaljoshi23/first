n=int(input())
divisors=set()
lst=[]
for i in range(n):
	a=int(input())
	lst.append(a)
for i in range(n):
	for j in range(1,lst[i]-1):
		if(lst[i]%(j)==0):
			divisors.add(j)

count=len(divisors)

if(count%2==0):
    print("JASBIR")
else:
    print("AMAN")