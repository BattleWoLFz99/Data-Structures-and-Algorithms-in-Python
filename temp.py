def print_n(n):
    if n <= 0:
        return

    print(n)
    print_n(n - 1)

print_n(6)