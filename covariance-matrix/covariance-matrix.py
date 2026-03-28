import numpy as np

def covariance_matrix(X):
    try:
        arr = np.array(X, dtype=float)
        
        if arr.ndim != 2:
            return None
        
        if arr.shape[0] < 2:
            return None
        
        if np.isnan(arr).any():
            return None
        
        cov = np.cov(arr, rowvar=False)
        
        return np.atleast_2d(cov)   # ✅ FIX
    
    except:
        return None