#!/usr/bin/python3


def fibo(n):
    if n == 1:
        return 1
    return n * fibo(n - 1)


if __name__ == "__main__":
    print(fibo(5))
