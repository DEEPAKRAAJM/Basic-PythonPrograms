############### Creating the Excel file and saving data in it ################
################# Inserting date and time in the Excel File ###################

import xlsxwriter # Library for creating a excel file
import datetime   # Library for inserting date and time
import time       # Library for inserting delay
                    
workbook = xlsxwriter.Workbook('Excel_file.xlsx') # Creating a new excel  file
worksheet = workbook.add_worksheet() # Adding worksheet

bold = workbook.add_format({'bold': True}) # Defining a format

worksheet.write('A1', 'DateTime', bold) # Assigning a lable in a cell 

row = 1  # Assigning row value
col = 0  # Assigning Column value

for i in range(0,11):
    date = datetime.datetime.now() # importing date and time 
    dd= str(date)   # Converting imported date and time into string
    time.sleep(2)
    worksheet.write(row, col, dd)
    row= row+1
workbook.close()
