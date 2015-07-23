print ("Please enter a grade for the assignment. (e.g. 70, 90, 50, 10, 0)")
grade = int(raw_input())

# check grade and give lettergrade
if grade >= 90: lettergrade = "A"
if grade >= 80 and not grade > 90: lettergrade = "B"
if grade >= 70 and not grade > 80: lettergrade = "C"
if grade <= 60 and not grade < 40: lettergrade = "D"
if grade <= 40: lettergrade = "F"

print(lettergrade)