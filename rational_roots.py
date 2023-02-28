import math

# Get the leading coefficient and constant term from the user
a = int(input("Enter the leading coefficient: "))
b = int(input("Enter the constant term: "))

# Find the possible rational roots
factors_of_a = [i for i in range(1, abs(a) + 1) if a % i == 0]
factors_of_b = [i for i in range(1, abs(b) + 1) if b % i == 0]

possible_roots = set()
for x in factors_of_b:
    for y in factors_of_a:
        possible_roots.add(x / y)
        possible_roots.add(-x / y)
        possible_roots.add(x / -y)

# Print the possible rational roots
print("The possible rational roots are:", possible_roots)
