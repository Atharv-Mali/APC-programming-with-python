items = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4]
visited = []

for item in items:
    if item not in visited:
        count = 0
        for value in items:
            if value == item:
                count += 1
        print(item, ":", count)
        visited.append(item)
