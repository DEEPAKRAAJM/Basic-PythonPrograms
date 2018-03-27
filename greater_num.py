#### Python Code for finding the Greatest of three numbers ######

num1= input("Enter the NO")
num2= input("Enter the NO")
num3= input("Enter the NO")
print "Entered Num are {0} {1} {2}".format(num1, num2, num3)

if num1>num2 and num1>num3:
	print "the Greatest no is:", num1
elif num2>num3 and num2>num1:
	print "the greatest no is: ", num2
else:
	print "the greatest no is: ", num3 