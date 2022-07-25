# Python program to display the Fibonacci sequence

def main():
    fib = get_fibonacci(8)
    print("Fibonacci is :{}".format(fib))


def get_fibonacci(n):
    f = 0
    f0 = 1
    f1 = 1
    while n > 1:
        n = n - 1
        f = f0 + f1
        f0 = f1
        f1 = f
    return f


if __name__ == '__main__':
    main()
