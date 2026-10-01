def matrix_dot_vector(a: list[list[int|float]], b: list[int|float]) -> list[int|float]:
    # Check that matrix is non-empty and columns match vector length
    if not a or not a[0]:
        return -1
    if len(a[0]) != len(b):
        return -1

    result = []
    for row in a:
        dot = 0
        for i in range(len(b)):
            dot += row[i] * b[i]
        result.append(dot)
    return result