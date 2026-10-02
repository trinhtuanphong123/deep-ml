def dice_statistics(n: int) -> tuple[float, float]:
    """
    Compute the expected value and variance of a fair n-sided die roll.

    Args:
        n (int): Number of sides of the die

    Returns:
        tuple: (expected_value, variance)
    """
    # Expected value: E[X] = (1 + 2 + ... + n) / n = (n + 1) / 2
    expected_value = (n + 1) / 2
    
    # Variance: Var(X) = E[X²] - (E[X])²
    # E[X²] = (1² + 2² + ... + n²) / n = n(n+1)(2n+1) / (6n) = (n+1)(2n+1) / 6
    expected_square = (n + 1) * (2 * n + 1) / 6
    variance = expected_square - expected_value ** 2
    
    return (expected_value, variance)