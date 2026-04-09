import numpy as np
import math

def poisson_pmf_cdf(lam, k):
    """
    Compute Poisson PMF and CDF.
    
    Parameters:
    lam : float (λ, mean rate)
    k   : int   (number of events)
    
    Returns:
    pmf : float
    cdf : float
    """
    # PMF
    pmf = (np.exp(-lam) * lam**k) / math.factorial(k)
    
    # CDF
    cdf = sum((np.exp(-lam) * lam**i) / math.factorial(i) for i in range(k + 1))
    
    return pmf, cdf