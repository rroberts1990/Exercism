def factors(value):
    divisor = 2
    prime_factors = []
    while value != 1:
        if value % divisor == 0:
            value /= divisor
            prime_factors.append(divisor)
        else:
            divisor += 1
    return prime_factors

