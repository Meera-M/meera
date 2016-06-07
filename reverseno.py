n=int(input("enter the number"))
rec=0
while(n>0):
	rem=n%10
	rec=(rec*10)+rem
	n=int(n/10)
	print(rec)
