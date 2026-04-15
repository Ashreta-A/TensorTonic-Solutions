import numpy as np

def bootstrap_mean(x, n_bootstrap=1000, ci=0.95, rng=None):
    """
    Returns: (boot_means, lower, upper)
    """
    x = np.asarray(x)
    
    # Random number generator
    if rng is None:
        rng = np.random.default_rng()
    
    n = len(x)
    
    # Generate bootstrap samples and compute means
    boot_means = np.array([
        np.mean(rng.choice(x, size=n, replace=True))
        for _ in range(n_bootstrap)
    ])
    
    # Confidence interval
    alpha = 1 - ci
    lower = np.percentile(boot_means, 100 * (alpha / 2))
    upper = np.percentile(boot_means, 100 * (1 - alpha / 2))
    
    return boot_means, lower, upper