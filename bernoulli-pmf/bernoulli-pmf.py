import numpy as np

def bernoulli_pmf_and_moments(x, p):
    try:
        # Validate p
        if p < 0 or p > 1:
            raise ValueError("Invalid probability")
        
        x = np.array(x)
        
        # Validate x values (must be 0 or 1)
        if not np.all((x == 0) | (x == 1)):
            raise ValueError("x must contain only 0 or 1")
        
        # PMF
        pmf = np.where(x == 1, p, 1 - p)
        
        # Moments
        mean = p
        variance = p * (1 - p)
        
        return pmf, mean, variance
    
    except:
        return None