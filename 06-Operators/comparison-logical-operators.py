a, b = 5, 10
print(a > b)  # False
print(a == b)  # False
print(a != b and a < b)  # True

#More Example

x = 10
y = 5
z = 15

# Using 'and' - both conditions must be True
print((x > y) and (x < z))  # True
print((x > y) and (x > z))  # False

# Using 'or' - at least one condition must be True
print((x < y) or (x > z))   # False
print((x > y) or (x > z))   # True

# Using 'not' - reverses the result
print(not(x > y))  # False (because x > y is True, and 'not' reverses it)
