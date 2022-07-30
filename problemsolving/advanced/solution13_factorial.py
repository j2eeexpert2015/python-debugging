# Factorial function:
def factorial(n):
    ans = n  # set initial value of answer before loop
    while n > 1:
        ans = ans * (n - 1)
        n = n - 1
        return ans
# main function
input = 0
fact = factorial(input)
print(fact)