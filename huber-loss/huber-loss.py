import numpy as np

def huber_loss(y_true, y_pred, delta=1.0):
    """
    Compute Huber Loss for regression.
    """
    # Convert to numpy arrays
    y_true = np.array(y_true)
    y_pred = np.array(y_pred)
    
    error = y_true - y_pred
    abs_error = np.abs(error)
    
    quadratic = np.minimum(abs_error, delta)
    linear = abs_error - quadratic
    
    loss = 0.5 * quadratic**2 + delta * linear
    
    return np.mean(loss)