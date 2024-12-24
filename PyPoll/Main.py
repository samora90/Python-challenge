# -*- coding: UTF-8 -*-
"""PyPoll Homework Starter File."""

# Import necessary modules
import csv
import os

# Files to load and output (update with correct file paths)
file_to_load = os.path.join("Resources", "election_data.csv")  # Input file path
file_to_output = os.path.join("analysis", "election_analysis.txt")  # Output file path

# Initialize variables to track the election data
total_votes = 0 
candidates = {}
winner = ""
max_votes = 0

# Open the CSV file and process it
with open(file_to_load) as election_data:
    reader = csv.reader(election_data)
    header = next(reader)

    # Loop through each row of the dataset and process it
    for row in reader:
        total_votes +=1
        candidate = row [2]

    if candidate not in candidates: 
             candidates [candidate] = 0
    candidates [candidate] += 1
    results = []
    for candidate, votes in candidates.items():
        percentage = (votes/total_votes) * 100
        results.append(f"{candidate}:{percentage:.3f}% ({votes})")
        if votes > max_votes:
             max_votes = votes
             winner = candidate


print("Election Results")  
print(".........................")  
print(f"Total Votes: {total_votes}")   
print(".........................") 
print("\n" .join(results))   
print(".........................")
print(f"Winner : {winner}")
print(".........................")


