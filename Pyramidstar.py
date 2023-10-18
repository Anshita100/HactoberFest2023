def pyramid_stars(n):
    for i in range(1, n + 1):
        print(" " * (n - i) + "*" * (2 * i - 1))

n = 5  # Number of rows
pyramid_stars(n)
