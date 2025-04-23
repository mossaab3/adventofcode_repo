import numpy as np 
import csv

def write_list_to_csv(file_name, data):
    with open(file_name, mode='w', newline='') as file:
        writer = csv.writer(file)
        for item in data:
            writer.writerow([item])
    print(f"Data written to {file_name}")



def is_safe(report):
    diffs = [b - a for a, b in zip(report, report[1:])]
    
    if all(d > 0 for d in diffs) or all(d < 0 for d in diffs):
        if all(1 <= abs(d) <= 3 for d in diffs):
            return True
    return False

def count_safe_reports(reports, with_dampener=False):
    safe_count = 0
    for report in reports:
        if is_safe(report):
            safe_count += 1
        elif with_dampener:
            for i in range(len(report)):
                modified = report[:i] + report[i+1:]
                if is_safe(modified):
                    safe_count += 1
                    break

        
    return safe_count

# Read your input as a list of lists of integers
# with open("input.txt") as f:
#     lines = f.read().strip().split("\n")
#     reports = [list(map(int, line.split())) for line in lines]

data = []
with open('advent_2_data.csv', 'r') as file:
    for line in file:
        row = list(map(int, line.strip().split()))
        data.append(row)

reports = np.array(data, dtype=object)

# Part One
print("Part 1 Safe Reports:", count_safe_reports(reports))

# Part Two
print("Part 2 Safe Reports with Dampener:", count_safe_reports(reports, with_dampener=True))