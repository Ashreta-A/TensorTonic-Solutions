import numpy as np

def matrix_inverse(A):
    try:
        A = np.array(A)
        
        # Check square
        if A.ndim != 2 or A.shape[0] != A.shape[1]:
            return None
        
        return np.linalg.inv(A)
    
    except np.linalg.LinAlgError:
        return None