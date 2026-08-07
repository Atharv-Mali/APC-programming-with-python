temperatures = [32, 35, 31, 30, 29, 33, 34, 36, 37, 38, 39, 40, 34, 33, 32, 31, 30, 29, 28, 27, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38]

hottest_day = 1
coldest_day = 1
highest_temp = temperatures[0]
lowest_temp = temperatures[0]
total = 0

for i in range(len(temperatures)):
    temp = temperatures[i]
    total += temp
    if temp > highest_temp:
        highest_temp = temp
        hottest_day = i + 1
    if temp < lowest_temp:
        lowest_temp = temp
        coldest_day = i + 1

average = total / len(temperatures)
above_average_days = 0
below_average_days = 0

for temp in temperatures:
    if temp > average:
        above_average_days += 1
    elif temp < average:
        below_average_days += 1

print("Hottest day:", hottest_day)
print("Coldest day:", coldest_day)
print("Average temperature:", average)
print("Days above average temperature:", above_average_days)
print("Days below average temperature:", below_average_days)
