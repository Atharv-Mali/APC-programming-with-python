salaries = [25000, 32000, 48000, 51000, 62000, 28000, 75000, 45000, 53000, 29000]

highest = salaries[0]
lowest = salaries[0]
total = 0
above_50000 = []
below_30000 = []

for salary in salaries:
    if salary > highest:
        highest = salary
    if salary < lowest:
        lowest = salary
    total += salary
    if salary > 50000:
        above_50000.append(salary)
    if salary < 30000:
        below_30000.append(salary)

average = total / len(salaries)

print("Highest salary:", highest)
print("Lowest salary:", lowest)
print("Average salary:", average)
print("Employees earning above 50000:", above_50000)
print("Employees earning below 30000:", below_30000)
