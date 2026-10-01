def transpose_matrix(a: list[list[int|float]]) -> list[list[int|float]]:   
    if not a  or not a[0]:
        return []

    rows = len(a)
    cols = len(a[0])

    result = [[0] * rows for _ in range(cols)]

    for i in range(rows):
        for j in range(cols):
            result[j][i] = a[i][j]
    
    return result