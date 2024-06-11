import os
import csv

# Set path for file
csvpath = "PyBank/Resources/budget_data.csv"

# variables
number_months = 0
total_profit = 0
last_month_profit = 0
changes = []
month_changes = []

# Open the CSV using the UTF-8 encoding
with open(csvpath, encoding='UTF-8') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    # Read the header row first (skip this step if there is no header)
    csv_header = next(csvreader)
    print(f"CSV Header: {csv_header}")

    # count the number of months (actually counting row of data)
    for row in csvreader:
        number_months += 1
        # print(row)

        #add profit
        

        # add profits and losses to find net total

        # create a list of changes in profit/losses and return the average change

        # if first row, there is no change
        if (number_months == 1):
            last_month_profit = int(row[1])
        else:
            change = int(row[1]) - last_month_profit
            changes.append(change)
            month_changes.append(row[0])

            last_month_profit = int(row[1])



        # greatest increase in profits

        # greatest decrease in profits
    

print("\nFinancial Analysis \n\n----------------------------\n")
print("\nTotal Months: ", number_months)

total_profit = total_profit, int(row[1])
print("\nTotal: ")

avg_change = sum(changes) / len(changes)
print("\nAverage Change: ", avg_change)


print("\nGreatest Increase in Profits: ")
print("\nGreatest Decrease in Profits: \n")
