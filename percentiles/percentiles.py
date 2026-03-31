import numpy as np

def percentiles(x, q):
    try:
        x = np.array(x, dtype=float)
        
        # Validate q
        if np.any((np.array(q) < 0) | (np.array(q) > 100)):
            return None
        
        return np.percentile(x, q, method='linear')
    
    except:
        return None