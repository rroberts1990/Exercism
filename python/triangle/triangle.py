def is_valid(sides):
    a, b, c = sides
    if any(sides) == 0:
        return False
    else:
        return not any([(a + b <= c) or (a + c <= b) or (b + c <= a)])

def equilateral(sides):
    unique_sides = set(sides)
    return len(unique_sides) == 1 and is_valid(sides)


def isosceles(sides):
    unique_sides = set(sides)
    return len(unique_sides) < 3 and is_valid(sides)


def scalene(sides):
    unique_sides = set(sides)
    return len(unique_sides) == 3 and is_valid(sides)
