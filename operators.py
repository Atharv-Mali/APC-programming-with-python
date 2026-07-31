a = 10
b = 3

print("Addition :", a + b)
print("Subtraction :", a - b)
print("Multiplication :", a * b)
print("Division :", a / b)
print("Floor Division :", a // b)
print("Modulus :", a % b)
print("Exponent :", a ** b)

print("Equal To :", a == b)
print("Not Equal To :", a != b)
print("Greater Than :", a > b)
print("Less Than :", a < b)
print("Greater Than or Equal To :", a >= b)
print("Less Than or Equal To :", a <= b)

x = a
print("Assignment :", x)

x += b
print("Add Assignment (+=) :", x)

x -= b
print("Subtract Assignment (-=) :", x)

x *= b
print("Multiply Assignment (*=) :", x)

x /= b
print("Divide Assignment (/=) :", x)

x //= 2
print("Floor Divide Assignment (//=) :", x)

x %= 2
print("Modulus Assignment (%=) :", x)

x **= 3
print("Exponent Assignment (**=) :", x)

print("Logical AND :", a > 5 and b < 5)
print("Logical OR :", a < 5 or b < 5)
print("Logical NOT :", not(a > b))

print("Bitwise AND :", a & b)
print("Bitwise OR :", a | b)
print("Bitwise XOR :", a ^ b)
print("Bitwise NOT :", ~a)
print("Left Shift :", a << 1)
print("Right Shift :", a >> 1)

list1 = [10, 20, 30]

print("Membership (in) :", 20 in list1)
print("Membership (not in) :", 40 not in list1)

list2 = list1
list3 = [10, 20, 30]

print("Identity (is) :", list1 is list2)
print("Identity (is not) :", list1 is not list3)
