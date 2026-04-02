import numpy as np
from scipy.special import comb

def binomial_pmf_cdf(n, p, k):
    try:
        # Validate inputs
        if not (0 <= p <= 1):
            return None
        if n < 0 or k < 0 or k > n:
            return None
        
        # PMF
        pmf = comb(n, k) * (p**k) * ((1-p)**(n-k))
        
        # CDF
        cdf = 0
        for i in range(0, k+1):
            cdf += comb(n, i) * (p**i) * ((1-p)**(n-i))
        
        return float(pmf), float(cdf)
    
    except:
        return None