#### Printing a number pattern ####
'''n =input("Enter numo of rows: ")
i=j=1
for i in range (0,n):
	num=1
	for j in range (0,i):
		print (num)
		num=num+1 '''

def pat(n):
	i=j=1
	for i in range (0,n):
		num=1
		for j in range (0,i):
			print (num)
			num=num+1
		print ("\r")
n=input ("Enter the no: ")
pat (n)
	

