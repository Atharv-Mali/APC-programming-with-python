marks = [78, 90, 56, 88, 67, 92, 74, 81, 69, 95, 60, 73, 84, 91, 58, 77, 66, 89, 93, 72]

highest = marks[0]
lowest = marks[0]
total = 0

for mark in marks:
    if mark > highest:
        highest = mark
    if mark < lowest:
        lowest = mark
    total += mark

average = total / len(marks)
above_average = 0
below_average = 0

for mark in marks:
    if mark > average:
        above_average += 1
    elif mark < average:
        below_average += 1

print("Highest marks:", highest)
print("Lowest marks:", lowest)
print("Average marks:", average)
print("Students above average:", above_average)
print("Students below average:", below_average)
