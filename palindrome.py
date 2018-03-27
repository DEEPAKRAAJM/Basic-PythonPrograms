###### Python Code to find the number is palindrome or not ########

str=raw_input("Enter the NO: ")
str1=str
str2= reversed(str) #Reversing a string
if list(str1) == list(str2): # list() is used for creating iterable string
	print "Palindrome"
else:
	print "Not"