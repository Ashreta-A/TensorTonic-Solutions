import numpy as np

def normalize_3d(v):
    """
    Normalize 3D vector(s) to unit length.
    
    Parameters:
    v : array-like
        Shape (3,) for single vector or (n,3) for multiple vectors
    
    Returns:
    normalized vector(s) with same shape
    """
    v = np.array(v, dtype=float)
    
    # Compute norms
    norms = np.linalg.norm(v, axis=-1, keepdims=True)
    
    # Avoid division by zero
    norms[norms == 0] = 1
    
    return v / norms