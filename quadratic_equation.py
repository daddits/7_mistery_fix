from math import sqrt


def get_roots(a, b, c):
    discriminant = b ** 2 - 4 * a * c
    if discriminant < 0:
    	return None, None  
    FERST_ROOT = (-b - sqrt(discriminant)) / (2 * a)
    SECOND_ROOT = (-b + sqrt(discriminant)) / (2 * a)
    if discriminant == 0:
        return FERST_ROOT, None  
    else:
        return FERST_ROOT, SECOND_ROOT 