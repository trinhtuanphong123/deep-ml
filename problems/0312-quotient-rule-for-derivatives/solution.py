import numpy as np

def quotient_rule_derivative(g_coeffs: list, h_coeffs: list, x: float) -> float:
    g, h = np.array(g_coeffs, dtype=float), np.array(h_coeffs, dtype=float)
    g_x, h_x = np.polyval(g, x), np.polyval(h, x)
    g_prime = np.polyder(g)
    h_prime = np.polyder(h)
    g_prime_x, h_prime_x = np.polyval(g_prime, x), np.polyval(h_prime, x)
    return (g_prime_x * h_x - g_x * h_prime_x) / (h_x ** 2)