# Recursion is a function which calls itself.
# It is used to directly use a mathematical formula as a function.


# factorial of a number
# 0! = 1
# 1! = 1
# 2! = 1 * 2

# 3! = 1 * 2 * 3

# 4! = 1 * 2 * 3 * 4
# 4! = 3! * 4

# n! = 1 * 2 * 3 *......n

# n! = 3! * .....n
# n! = (n-1)! * n


# n = 3

# multiply = 1
# for i in range(n):
#     multiply = multiply * (i+1)
# print(multiply)


# function creation
def factorial_loops(n):
    multiply = 1
    for i in range(n):
        multiply = multiply * (i+1)
    return(multiply)

# # function calling
# f = factorial_loops(3)
# f1 = factorial_loops(4)
# f3 = factorial_loops(6)
# print(f , f1)
# print(f3)


def factorial_recursion(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial_recursion(n-1)


f2 = factorial_recursion(4)
print(f2)