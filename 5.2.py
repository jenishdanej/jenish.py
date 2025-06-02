

a = float(input("Enter first number: "))
b = float(input("Enter second number: "))
c = float(input("Enter third number: "))
d = float(input("Enter fourth number: "))

if a < b:
    if a < c:
        if a < d:
            minimum = a
        else:
            minimum = d
    else:
        if c < d:
            minimum = c
        else:
            minimum = d
else:
    if b < c:
        if b < d:
            minimum = b
        else:
            minimum = d
    else:
        if c < d:
            minimum = c
        else:
            minimum = d

# Output the result
print("The minimum number is:", minimum)
