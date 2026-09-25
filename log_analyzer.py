"""
Robot Log Analyzer
-------------------
Reads a robot shift log and checks each line for common problem
indicators (errors, low battery, high temperature readings).
Prints a status for every line and a total problem count at the end.
"""

log_file = open("end_shift.log", "r")

problem_count = 0

for line in log_file:
    line = line.strip()

    if "ERROR" in line:
        print("Problem Found:", line)
        print("Suggested Action: Check robot and investigate error")
        problem_count += 1

    elif "Low" in line:
        print("Problem Found:", line)
        print("Suggested Action: Check battery level")
        problem_count += 1

    elif "High" in line:
        print("Problem Found:", line)
        print("Suggested Action: Check system reading")
        problem_count += 1

    else:
        print("Status OK:", line)

log_file.close()

print("Total Problems:", problem_count)
