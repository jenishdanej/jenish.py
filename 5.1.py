


a = float(input("Enter first number: "))
b = float(input("Enter second number: "))
c = float(input("Enter third number: "))


if a < b:
    if a < c:
        minimum = a
    else:
        minimum = c
else:
    if b < c:
        minimum = b
    else:
        minimum = c

# Output the result
print("The minimum number is:", minimum)
