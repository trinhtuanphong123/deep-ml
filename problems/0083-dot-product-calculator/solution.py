import numpy as np

def calculate_dot_product(vec1, vec2):
    if len(vec1) != len(vec2):
        return False
    else:
        result = 0
        for i in range(len(vec1)):
            result += vec1[i] * vec2[i]
        return result