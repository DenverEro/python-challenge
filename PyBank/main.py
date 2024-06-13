import os
import csv

# Set path for file
csvpath = "Resources/budget_data.csv"

# Variables
number_months = 0
total_profit = 0
last_month_profit = 0
changes = []
month_changes = []

# Open the CSV using the UTF-8 encoding
with open(csvpath, encoding='UTF-8') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    # Read the header row first
    csv_header = next(csvreader)

    # Process each row in the CSV
    for row in csvreader:
        number_months += 1 # increment number of months
        current_month_profit = int(row[1]) # convert profit/loss to integer
        total_profit += current_month_profit # add each month to the running total

        if number_months > 1: # start after the first month
            change = current_month_profit - last_month_profit # find the monthly difference 
            changes.append(change) # add this number to a list called "changes"
            month_changes.append(row[0]) # associated month added to another list

        last_month_profit = current_month_profit # update last_month_profit to current month's profit

# Calculate average change
average_change = sum(changes) / len(changes) if changes else 0

# Find greatest increase and decrease in profits
greatest_increase = max(changes) if changes else 0
greatest_decrease = min(changes) if changes else 0

# Find the corresponding months for greatest increase and decrease
greatest_increase_month = month_changes[changes.index(greatest_increase)] if changes else ''
greatest_decrease_month = month_changes[changes.index(greatest_decrease)] if changes else ''

# Prepare the output
output = (
    f"\nFinancial Analysis\n"
    f"\n----------------------------\n"
    f"\nTotal Months: {number_months}\n"
    f"\nTotal: ${total_profit}\n"
    f"\nAverage Change: ${average_change:.2f}\n"
    f"\nGreatest Increase in Profits: {greatest_increase_month} (${greatest_increase})\n"
    f"\nGreatest Decrease in Profits: {greatest_decrease_month} (${greatest_decrease})\n"
)

# Print the output to the terminal
print(output)

# Export the results to a text file
with open('Analysis/financial_analysis.txt', 'w') as textfile:
    textfile.write(output)