import math

# Get the leading coefficient and constant term from the user
# a = int(input("Enter the leading coefficient: "))
# b = int(input("Enter the constant term: "))
# expression = input(
#     "Enter the expression in the form ax + b = 0: "
# )

# test vbalues

a = 1
b = 7
expression = "x^4-5x^3-8x^2+5x+7"

# replace all occurences of ^ with **
expression = expression.replace("^", " ** ")

# Add * before each x that doesn't already have an operator in front
expression = (
    expression.replace("x", "*x")
    .replace("+-", "-")
    .replace("--", "+")
    .replace("-+", "-")
    .replace("++", "+")
)
# delete a leading operator
if expression[0] in ["+", "-", "*", "/", "^", "**"]:
    expression = expression[1:]


# Find the possible rational roots
factors_of_a = [i for i in range(1, abs(a) + 1) if a % i == 0]
factors_of_b = [i for i in range(1, abs(b) + 1) if b % i == 0]

possible_roots = set()
for x in factors_of_b:
    for y in factors_of_a:
        possible_roots.add(x / y)
        possible_roots.add(-x / y)
        possible_roots.add(x / -y)


if expression != "":
    # Find the rational roots
    rational_roots = set()
    for root in possible_roots:
        x = int(root)
        result = eval(expression)
        if result == 0:
            rational_roots.add(root)

    # Print the rational roots
    print("The rational roots are:", rational_roots)

# Print the possible rational roots
print("The possible rational roots are:", possible_roots)
