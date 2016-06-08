l=int(input())
u=int(input())
f=0
for i in range(2,u+1):
	if i > 0:
		for j in range(2,i):
			if (i % j) == 0:
				break
		else:
			f=f+1
print(f)
