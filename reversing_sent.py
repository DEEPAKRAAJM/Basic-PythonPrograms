#### Python code to Reverse the statement #####

str= input("Enter the statement")
first=str.split(" ")  # the split() function is used for seperating the words in the statement
last= first[::-1]
print(last)