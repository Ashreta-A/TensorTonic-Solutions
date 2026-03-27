import numpy as np
import math

import numpy as np

def cosine_similarity(a, b):
    norm_a = np.linalg.norm(a)
    norm_b = np.linalg.norm(b)
    
    # Check for zero division
    if norm_a == 0 or norm_b == 0:
        return 0   # or you can return None
    
    return np.dot(a, b) / (norm_a * norm_b)