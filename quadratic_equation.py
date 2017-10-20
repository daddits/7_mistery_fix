from math import sqrt


def get_roots(a, b, c):
    discriminant = b ** 2 - 4 * a * c
    if discriminant < 0:
    	return None, None  
    ferst_root = (-b - sqrt(discriminant)) / (2 * a)
    second_root = (-b + sqrt(discriminant)) / (2 * a)
    if discriminant == 0:
        return ferst_root, None  
    else:
        return ferst_root, second_root