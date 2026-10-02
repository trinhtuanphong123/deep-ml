import numpy as np

def gradient_direction_magnitude(gradient: list) -> dict:
    """
    Calculate the magnitude and direction of a gradient vector.
    
    Args:
        gradient: A list representing the gradient vector
    
    Returns:
        Dictionary containing:
        - magnitude: The L2 norm of the gradient
        - direction: Unit vector in direction of steepest ascent
        - descent_direction: Unit vector in direction of steepest descent
    """
    # Convert to numpy array for easier computation
    grad_array = np.array(gradient)
    
    # Calculate magnitude (L2 norm)
    magnitude = np.linalg.norm(grad_array)
    
    # Handle zero vector case
    if magnitude == 0:
        # Zero vector - no direction
        direction = np.zeros_like(grad_array).tolist()
        descent_direction = np.zeros_like(grad_array).tolist()
    else:
        # Normalize to get unit vector (direction of steepest ascent)
        direction = (grad_array / magnitude).tolist()
        # Descent direction is opposite of ascent direction
        descent_direction = (-grad_array / magnitude).tolist()
    
    return {
        'magnitude': float(magnitude),
        'direction': direction,
        'descent_direction': descent_direction
    }