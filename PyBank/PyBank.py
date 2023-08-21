#!/usr/bin/env python
# coding: utf-8

# In[10]:


import csv
import os


Budget_File = os.path.join(".", "Resources", "budget_data.csv")

#Creating a "Budget Analysis to store output"
Budget_Output = os.path.join(".", "Budget_Analysis.txt")



Total_Months = 0
Total = 0
Average_Change = 0.0
Net_Change_List = []
Greatest = ["", 0]
Least = ["", 9999999999]


# Read cvs and convert it into a list

with open(Budget_File) as Financial_Data:
    
    reader = csv.reader(Financial_Data)

    
# removing header from the data to do analysis and calculation
    header = next(reader)
    First_Row = next(reader)
    Total = Total + int(First_Row[1])
    Previous_Row_Value = int(First_Row[1])

    
#To calculate Avarage Change :
#Track the change by store value of previuos row and then subtract it from next row and update previous row with new value.
#Create a List of changes
#Add all the values of the list and divide by total count of the list
 
    
    for row in reader:
        Total_Months = Total_Months + 1
        
        Total = Total + int(row[1])
        
        Change_In_Value = int(row[1]) - Previous_Row_Value
        
        Previous_Row_Value = int(row[1])
        
        Net_Change_List.append(Change_In_Value)
            
#Calculate Greates Change 

        if(Change_In_Value > Greatest[1]):
            Greatest[0] = row[0]
            Greatest[1] = Change_In_Value 
            
            
#Calculate Lowest Change        
        if(Change_In_Value < Least[1]):
            Least[0] = row[0]
            Least[1] = Change_In_Value

            
            
            
        
    Average_Change = sum(Net_Change_List)/len(Net_Change_List)
   
       
Output = (
        f"Financial Analysis\n"
        f"------------------------------------\n"
        f'Total Months: {Total_Months}\n'
        f'Total : {Total}\n'
        f"Average Change : ${Average_Change: .2f}\n"
        f'Greatest Increase in Profits : {Greatest}\n'
        f'Greatest Decrease in Profits : {Least}')
print(Output)



with open(Budget_Output, "w") as txt_file:
    txt_file.write(Output)



# In[ ]:





# In[ ]:




