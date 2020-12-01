def steps(n):
    if n <= 0:
        raise ValueError("Starting number must be greater than zero")
    s = 0
    while n != 1:
        n = n/2 if n % 2 == 0 else n*3 + 1
        s += 1
    return s
