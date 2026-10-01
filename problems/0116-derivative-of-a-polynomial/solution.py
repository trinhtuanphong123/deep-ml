def poly_term_derivative(c: float, x: float, n: float) -> float:
    # Compute x^(n-1) with a loop
    result = 1.0
    i = 0
    while i < n - 1:
        result *= x
        i += 1
    return c * n * result