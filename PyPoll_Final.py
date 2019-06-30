# Import the os module
import os

# Module for reading CSV files
import csv

csvpath = os.path.join("election_data.csv")
with open(csvpath, newline='') as csvfile:
    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')
    csv_header = next(csvreader)

    # create variables
    votes = 0
    candidates = []
    vote_counts = []
    max_votes = 0
    winner = ""

    # Read each row of data after the header
    for row in csvreader:
    # start loop for vote counts and candidate totals
        votes += 1
        if row[2] not in candidates:
            candidates.append(row[2])
            vote_counts.append(1)
        else:
            for i in range(len(candidates)):
                if candidates [i] == row[2]:
                    vote_counts [i] += 1
                if vote_counts [i] > max_votes: 
                    max_votes = vote_counts[i]
                    winner = candidates [i]
    
    print("Election Results")
    print("___________________")
    print("Total Votes: " + str(votes))
    print("___________________")
    for i in range(len(candidates)):
        print(str(candidates[i])+": " + str(round(vote_counts[i]*100/votes))+".000% ("+ str(vote_counts[i])+")")
    print("___________________")
    print("Winner: " + winner)       
    print("___________________")


