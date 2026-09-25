# Robot Log Analyzer

A small Python script that simulates checking a robot's end-of-shift log for
common issues — errors, low battery, and high temperature readings — and
suggests a next action for each one.

## What it does

The script reads a log file line by line. For each line it checks for:

- `ERROR` → flags the issue and suggests investigating the robot
- `Low` → flags the issue and suggests checking the battery
- `High` → flags the issue and suggests checking the system reading
- Anything else → reported as normal status

At the end, it prints the total number of problems found across the shift.

## Example input (`end_shift.log`)

```
Trossen_01, Battery: 85, Status: Normal
Trossen_02, Battery: 14, Status: Low
Trossen_03, Camera: ERROR
Trossen_04, Temperature: High
Trossen_05, Battery: 72, Status: Normal
```

## Example output

```
Status OK: Trossen_01, Battery: 85, Status: Normal
Problem Found: Trossen_02, Battery: 14, Status: Low
Suggested Action: Check battery level
Problem Found: Trossen_03, Camera: ERROR
Suggested Action: Check robot and investigate error
Problem Found: Trossen_04, Temperature: High
Suggested Action: Check system reading
Status OK: Trossen_05, Battery: 72, Status: Normal
Total Problems: 3
```

## How to run it

```
python log_analyzer.py
```

(Make sure `end_shift.log` is in the same folder as the script.)

## Python concepts used

- Reading a file and looping through it line by line
- String searching with `in`
- `if` / `elif` / `else` branching
- Counters and variables
- `.strip()` for cleaning up each line
- Closing a file after use

## Why this is relevant to robotics operations

Robotics technicians and lab operators regularly review shift logs to catch
equipment issues early. This script models that workflow in a simple,
readable way — flagging the kind of battery, camera, and sensor issues that
come up in day-to-day robot data-collection and lab environments.
