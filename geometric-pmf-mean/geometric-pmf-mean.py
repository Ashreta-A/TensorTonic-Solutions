import numpy as np

def geometric_pmf_mean(k, p):
    """
    Compute Geometric PMF and Mean.
    
    k : int or list/array
    p : float
    """
    
    # Convert k to numpy array (handles both int and list)
    k = np.array(k)
    
    # PMF (element-wise if k is array)
    pmf = (1 - p)**(k - 1) * p
    
    # Mean
    mean = 1 / p
    
    return pmf, mean