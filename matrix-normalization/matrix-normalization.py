import numpy as np

def matrix_normalization(matrix, axis=None, norm_type='l2'):
    try:
        X = np.array(matrix, dtype=float)
        
        # Ensure 2D
        if X.ndim != 2:
            return None
        
        if np.isnan(X).any():
            return None
        
        if norm_type == 'l1':
            norm = np.sum(np.abs(X), axis=axis, keepdims=True)
        elif norm_type == 'l2':
            norm = np.sqrt(np.sum(X**2, axis=axis, keepdims=True))
        elif norm_type == 'max':
            norm = np.max(np.abs(X), axis=axis, keepdims=True)
        else:
            return None
        
        norm = np.where(norm == 0, 1, norm)
        
        return X / norm
    
    except:
        return None