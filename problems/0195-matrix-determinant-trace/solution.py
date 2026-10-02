def matrix_determinant_and_trace(matrix: list[list[float]]) -> tuple[float, float]:
    """
    Compute the determinant and trace of a square matrix.
    
    Args:
        matrix: A square matrix (n x n) represented as list of lists
    
    Returns:
        Tuple of (determinant, trace)
    """
    n = len(matrix)
    
    # Kiểm tra ma trận vuông
    if n == 0 or any(len(row) != n for row in matrix):
        raise ValueError("Matrix must be square and non-empty")
    
    # ===== TÍNH TRACE =====
    # Tổng các phần tử trên đường chéo chính: a[0][0] + a[1][1] + ... + a[n-1][n-1]
    trace = sum(matrix[i][i] for i in range(n))
    
    # ===== TÍNH DETERMINANT =====
    # Dùng khai triển Laplace (cofactor expansion) theo hàng đầu tiên
    def determinant(mat):
        size = len(mat)
        
        # Base cases
        if size == 1:
            return mat[0][0]
        if size == 2:
            return mat[0][0] * mat[1][1] - mat[0][1] * mat[1][0]
        
        # Khai triển theo hàng đầu tiên
        det = 0
        for j in range(size):
            # Tạo ma trận con bỏ hàng 0 và cột j
            minor = [row[:j] + row[j+1:] for row in mat[1:]]
            # Dấu xen kẽ: +, -, +, -, ...
            sign = (-1) ** j
            det += sign * mat[0][j] * determinant(minor)
        
        return det
    
    det = determinant(matrix)
    
    return (det, trace)