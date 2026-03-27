import numpy as np

def calculate_eigenvalues(matrix):
    try:
        n = np.array(matrix)
        
        # Check if matrix is 2D and square
        if n.ndim != 2 or n.shape[0] != n.shape[1]:
            return None
        
        return np.linalg.eigvals(n)
    
    except Exception:
        return None