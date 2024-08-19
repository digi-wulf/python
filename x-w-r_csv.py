# Create program that writes imputs to CSV file.
#
# 1. Allow user to write input to each section
# 2. Include header section in each csv
#

import os
import csv
os.system('cls')

fname = input('Enter new file name: ')
csvfile = open(f"{fname}.csv", "x")
csvfile.close()

# Creats header list based on input amount
header = []
head_amount = input("How many headers: ")
print("\n")

x = 0
while x < int(head_amount):
    headName = input(f"Enter header {x + 1}: ")
    header.append(headName)
    x += 1
print(header)

# Create list based on based on header and input row amount
rows = []
row = []
row_amount = input("How many rows: ")
print("\n")

x = 0
y = 0
while x < int(row_amount):
    while y < int(head_amount):
        row_input = input(f"Enter row {y + 1} field: ")
        row.append(row_input)
        print(rows)
        y += 1
    x += 1


# Writes to csv file
'''with open(f'{fname}.csv', 'w', newline = '') as file:
    writer = csv.writer(file)
    dw = csv.DictWriter(file, delimiter = ',', fieldnames = header) 
    dw.writeheader()'''
    