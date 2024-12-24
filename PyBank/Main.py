# -*- coding: UTF-8 -*-
"""PyBank Homework Starter File."""

# Dependencies
import csv
import os

# Files to load and output (update with correct file paths)
file_to_load = os.path.join("Resources", "budget_data.csv")  # Input file path
file_to_output = os.path.join("analysis", "budget_analysis.txt")  # Output file path

# Define variables to track the financial data
total_months = 0
total_net = 0
# Add more variables to track other necessary financial data
previous_profit = None
changes = []

greatest_increase = ["",0]
greatest_decrease = ["",999999]
# Open and read the csv
with open(file_to_load) as financial_data:
    reader = csv.reader(financial_data)

    # Skip the header row
    header = next(reader)

    # Extract first row to avoid appending to net_change_list
    first_raw = next(reader)
    total_months +=1
    total_net +=int(first_raw[1])
    previous_profit = int(first_raw[1])

    

    # Track the total and net change
    for row in reader:
       total_months +=1
       total_net+=int(row[1]) 
       net_change = int(row[1])-previous_profit
       previous_profit =int(row[1])
       changes.append(net_change)



        # Calculate the greatest increase in profits (month and amount)
       if  net_change > greatest_increase[1]:
            greatest_increase[0]=row[0]
            greatest_increase[1]=net_change

        # Calculate the greatest decrease in losses (month and amount)
       if  net_change < greatest_decrease[1]:
            greatest_decrease[0]=row[0]
            greatest_decrease[1]=net_change


# Calculate the average net change across the months
average_month_change = sum(changes)/len(changes)

# Generate the output summary
output_summary = (
    f"Financial Analysis\n"
    f"----------------------------\n"
    f"Total Months: {total_months}\n"
    f"Total: ${total_net}\n"
    f"Average Change: ${average_month_change:.2f}\n"
    f"Greatest increase in profits: {greatest_increase[0]} (${greatest_increase[1]})\n"
    f"Greatest decrease in losses: {greatest_decrease[0]} (${greatest_decrease[1]})\n")

# Print the output
print(output_summary)

# Write the results to a text file
with open(file_to_output, "w") as txt_file:
    txt_file.write(output_summary)
