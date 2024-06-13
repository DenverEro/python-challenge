import os
import csv

# Set path for file
csvpath = "Resources/election_data.csv"

# Variables
total_votes = 0
candidates = {}
winner = ""
max_votes = 0

# read the csv file and count votes
with open(csvpath, encoding='UTF-8') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    # Read the header row first
    csv_header = next(csvreader)

    # Process each row in the CSV
    for row in csvreader:
        total_votes += 1
        candidate = row[2] # access name in 3rd cell
        if candidate in candidates: # dictionary using names as keys, checks if name exists
            candidates[candidate] += 1 # if exists, add 1 to vote count
        else:
            candidates[candidate] = 1 # if not, add name to dictionary with vote count 1

# Prepare the output
output = (
    f"Election Results\n"
    f"\n-------------------------\n"
    f"\nTotal Votes: {total_votes}\n"
    f"\n-------------------------\n"
)
# Iterate through each candidate and their vote count
for candidate, votes in candidates.items():
    percentage = (votes / total_votes) * 100
    output += f"\n{candidate}: {percentage:.3f}% ({votes})\n"
    if votes > max_votes: # Check if the current candidate has the most votes
        max_votes = votes
        winner = candidate
output += (
    f"\n-------------------------\n"
    f"\nWinner: {winner}\n"
    f"\n-------------------------\n"
)

# Print the results to the terminal
print(output)

# Export the results to a text file
with open("Analysis/election_results.txt", "w") as textfile:
    textfile.write(output)
