###### Program for Calculating the Fibanacci Series #######

num= input("Enter the NO: ")
n=num
t1, t2, t3=0
for i in range(1, n):
	print t1
	t3=t1+t2
	t2=t3