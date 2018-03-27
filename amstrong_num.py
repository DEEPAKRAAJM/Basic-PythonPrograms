######### Program to find the given number is a Amstrong number or not ########
''' Armstrong Numbers are the numbers in which the sum of the qube of 
     the digits will be equal to the number '''
     
num=input("Enter any number >= 2 digits: ")
orgi=num
result=0
while orgi!=0:
	rem=orgi%10
	result+= rem*rem*rem
	orgi=orgi/10
if result == num:
	print num, "number is Amstrong no"
else:
	print "Not an amstrong no" 
