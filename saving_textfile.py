##### Storing the values of the iterations in a text file using the list function #########
### This list function is used to store multiple values without overwritting each other ###  
import cv2
a=0 
list=[] # Using list function to store the values
for i in range(0,10,1):
	a=a+i
	print("Sum:{}".format(a))
	b=open('textfile.txt','w') # Opening a new text file and enabling the writing of data to it.
	list.append(a)
	b.writelines(["Sum :%s\n" %list for j in range(0,1)]) # Writing the contents to the text file.
	b.close() # Closing the file once the data is entered.

