# Import the os module
import os

# Module for reading CSV files
import csv

csvpath = os.path.join("budget_data.csv")
with open(csvpath, newline='') as csvfile:
    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')

    print(csvreader)

    # Read the header row first (skip this step if there is now header)
    csv_header = next(csvreader)
    print(f"CSV Header: {csv_header}")

    # Read each row of data after the header
    for row in csvreader:
        print(row)

# variables
total_months = 0
total_amount = 0
avg_change_profloss = 0
greatest_increase = 0
greatest_decrease = 0

# other variables needed
last_profloss = 0
profloss = 0
month_changeprofloss = 0

# read csv file
with open(csvpath, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    header = next(csvreader)  
    for row in csvreader:
        # The total number of months included in the dataset
        total_months += 1 

        # The net total amount of "Profit/Losses" over the entire period
        total_amount += int(row[1]) 
        
        # The average of the changes in "Profit/Losses" over the entire period             
        if total_months == 1:
            month_changeprofloss = 0
            sum_changeprofloss = 0
            last_profloss=int(row[1])
        else: 
            month_changeprofloss = int(row[1])-last_profloss
            sum_changeprofloss += month_changeprofloss
            last_profloss=int(row[1])
            #avg_change_profloss = (total_amount - 867884 / (total_months - 1))
            
        # The greatest increase in profits (date and amount) over the entire period         
        if (month_changeprofloss > greatest_increase): 
            greatest_inc_date = row[0]
            greatest_increase = month_changeprofloss

        # The greatest decrease in losses (date and amount) over the entire period    
        elif (month_changeprofloss < greatest_decrease):
            greatest_dec_date = row[0]
            greatest_decrease = month_changeprofloss

    print("--------------------------------------------------")
    print(f"Total Months: {total_months}")
    print(f"Total Revenue: ${total_amount}")
    print(f"Averange Revenue Change: ${sum_changeprofloss / (total_months - 1)}")
    print(f"Greatest Increase in Revenue: {greatest_inc_date}, ${greatest_increase}")
    print(f"Greatest Decrease in Revenue: {greatest_dec_date}, ${greatest_decrease}")

