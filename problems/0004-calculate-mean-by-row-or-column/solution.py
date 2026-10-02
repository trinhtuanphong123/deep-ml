def calculate_matrix_mean(matrix: list[list[float]], mode: str) -> list[float]:
    """
    Calculate the mean of a matrix either by row or by column.
    
    Args:
        matrix: A 2D list of numbers (list of lists)
        mode: 'row' or 'column'
    
    Returns:
        List of means according to the specified mode
    """
    if not matrix or not matrix[0]:
        return []
    
    num_rows = len(matrix)
    num_cols = len(matrix[0])
    
    if mode == 'row':
        # Mean của mỗi hàng: trung bình cộng các phần tử trong hàng đó
        means = [sum(row) / num_cols for row in matrix]
    elif mode == 'column':
        # Mean của mỗi cột: trung bình cộng các phần tử trong cột đó
        means = [
            sum(matrix[i][j] for i in range(num_rows)) / num_rows
            for j in range(num_cols)
        ]
    else:
        raise ValueError("mode must be 'row' or 'column'")
    
    return means