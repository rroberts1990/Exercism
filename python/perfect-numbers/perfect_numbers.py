


def classify(number):
    if number < 1:
    	raise ValueError("Not a natural number")
    y = sum([i for i in range(1, number) if number % i == 0])
    if y == number:
        return "perfect"
    elif y > number:
        return "abundant"
    else:
        return "deficient"


classify(6)