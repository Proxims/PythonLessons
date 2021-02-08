# Lesson-14-Functions-part1


def napechatat_privetstvie(name):
    """Print Privetstvie"""
    print("Hello, " + name)
    print("Congratulations!")


def summa(x=input("Enter X: "), y=input("Enter Y: ")):
    return (int(x) + int(y))


def factorial(x):
    """Calculate factorial of number X"""
    otvet = 1
    for i in range(1, x + 1):
        otvet = otvet * i
    return otvet


# ------------------------------------
x = summa()
print("Factorial of number " + str(x) + " will be: ")
print(factorial(int(x)))
print("------------------------\n")

for i in range(1, 11):
    print(str(i) + "!\t" + str(factorial(i)))
