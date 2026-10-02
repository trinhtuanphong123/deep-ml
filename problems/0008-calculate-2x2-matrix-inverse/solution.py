def inverse_2x2(matrix: list[list[float]]) -> list[list[float]] | None:
    """
    Calculate the inverse of a 2x2 matrix.
    
    Args:
        matrix: A 2x2 matrix represented as [[a, b], [c, d]]
    
    Returns:
        The inverse matrix as a 2x2 list, or None if the matrix is singular
        (i.e., determinant equals zero)
    """
    a, b = matrix[0]
    c, d = matrix[1]
    
    # Tính định thức
    det = a * d - b * c
    
    # Kiểm tra ma trận khả nghịch
    if det == 0:
        return None
    
    # Công thức nghịch đảo: (1/det) * [[d, -b], [-c, a]]
    inv_det = 1.0 / det
    inverse = [
        [d * inv_det, -b * inv_det],
        [-c * inv_det, a * inv_det]
    ]
    
    return inverse