import numpy as np
def make_diagonal(v):
    try:
        v = np.array(v)
        if v.ndim != 1:
            return None
        return np.diag(v)
    except:
        return None