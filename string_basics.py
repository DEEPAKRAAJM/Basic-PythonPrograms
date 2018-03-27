##### Python Code describing different operations in string ######

str= raw_input("Enter a string: ") 
print 'string is: ', str[0] #First Char
print 'CHAR: ', str[-1] #Last Char
print 'CHAR: ', str[1:5] #Slicing in between
print 'CHAR: ', str[2:-2] #middle to second last
L=len(str)  #string length
print L
str2= raw_input("Enter another string: ") #Concatinating the string
print "Combined", str+str2
print(str*4) #Displaying multiple time
# enumerate()
list_enumerate = list(enumerate(str))
print "\n list(enumerate(str) = ", list_enumerate
print('len(str) = ', len(str))
print '''He asked "What's this?"''' # for displaying the " 's "
print str.lower() # Converting to lower case
print str.upper() # Converting to Upper Case