from math import sqrt


def get_roots(a, b, c):
    discriminant = b ** 2 - 4 * a * c
    if discriminant < 0:
        return None, None
    first_root = (-b - sqrt(discriminant)) / (2 * a)
    second_root = (-b + sqrt(discriminant)) / (2 * a)
    if discriminant == 0:
        return first_root, None
    else:
        return first_root, second_root
