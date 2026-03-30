import numpy as np
from collections import Counter

def mean_median_mode(x):
    try:
        x = np.array(x, dtype=float)
        
        # Mean
        mean = float(np.mean(x))
        
        # Median
        median = float(np.median(x))
        
        # Mode
        counts = Counter(x)
        max_freq = max(counts.values())
        
        # Get all modes
        modes = [k for k, v in counts.items() if v == max_freq]
        
        # Return smallest mode (scalar)
        mode = float(min(modes))
        
        return mean, median, mode
    
    except:
        return None