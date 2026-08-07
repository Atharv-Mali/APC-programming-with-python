items = [1, 2, 3, 4, 5]

left_rotated = items[1:] + items[:1]
right_rotated = items[-1:] + items[:-1]

print("Original list:", items)
print("Left rotated:", left_rotated)
print("Right rotated:", right_rotated)
