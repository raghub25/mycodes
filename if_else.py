
def animal(activity):
    if activity == "barks":
        return "dog"
    elif activity == "hiss":
        return "cat"
    else:
        return "Unknown"


# value = input("Enter the activity of the animal: ")
# print("It's a " + animal(value))


def divide(num1, num2, op):
    if op == "/":
        if num2 != 0:
            return num1 / num2
        else:
            return "Cannot divide by zero"
    else:
        return "Invalid operator"


n1 = float(input("Enter the first number: "))
operate = input("Enter the operation: ")
n2 = float(input("Enter the second number: "))
print(divide(n1, n2, operate))

