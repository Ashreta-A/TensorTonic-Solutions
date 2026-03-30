import numpy as np

def sample_var_std(x):
    try:
        x = np.array(x, dtype=float)
        
        n = len(x)
        if n < 2:
            return None
        
        mean = np.mean(x)
        
        # Sample variance
        var = np.sum((x - mean) ** 2) / (n - 1)
        
        # Standard deviation
        std = np.sqrt(var)
        
        return var, std
    
    except:
        return None