#Ryan Johnson
#Homework #2
# Add items to the program
import os
import csv


bank_csv = os.path.join("C:","/python_source_data","PyBank_budget_data.csv")

# Open the csv file

with open(bank_csv, newline="") as csvfile:

# Create csv reader 

    csvreader = csv.reader(csvfile, delimiter=",") 

# read the heading 

    csv_header = next(csvfile)


# The total number of months included in the dataset
    data = list(csvreader)
    row_count = len(data)



# re-reate csv reader 
with open(bank_csv, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",") 
    csv_header = next(csvfile)
    

   
    print(data)
    # The total net amount of "Profit/Losses" over the entire period
    # set variable defaults
    maxProfit = 0 
    maxLoss = 0
    total = 0
    delta = 0
    priorMonth = 0

# loop thorugh file
    for row in csv.reader(csvfile):
        total += int(row[1])
        If int(row[1]) - priorMonth

# The greatest increase in profits (date and amount) over the entire period        
        if int(row[1]) > maxProfit:
            maxProfit = int(row[1])
            maxProfitMonth = row[0]

# The greatest decrease in losses (date and amount) over the entire period            
        if int(row[1]) < maxLoss:
            maxLoss = int(row[1])
            maxLossMonth = row[0]  

# The average change in "Profit/Losses" between months over the entire period             
    averageMonth = int(total)/int(row_count)
    
    
# print results   
    print(maxProfit)
    print(maxLoss)
    print(maxProfitMonth)
    print(maxLossMonth)
    print(f"Total Months: ",str(row_count))
    print(total)
    print(averageMonth)

print("Financial Analysis")
print("----------------------------")
print(f'Total Months:',str(row_count))
print(f'Average Change: $',str(averageMonth))
print(f'Greatest Increase in Profits:',str(maxProfitMonth),'($',str(maxProfit),")")
print(f'Greatest Decrease in Profits:',str(maxLossMonth),'($',str(maxLoss),")")



# Financial Analysis
# ----------------------------
# Total Months: 86
# Total: $38382578
# Average  Change: $-2315.12
# Greatest Increase in Profits: Feb-2012 ($1926159)
# Greatest Decrease in Profits: Sep-2013 ($-2196167)


# In addition, your final script should both print the analysis to the terminal and export a text file with the results.