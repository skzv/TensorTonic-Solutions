import numpy as np

def expected_value_discrete(x, p):
    """
    Returns: float expected value
    """
    # Write code here
    if len(x) != len(p):
        raise ValueError("Dimensions of x and p do not match")
    
    x_p = np.array(p)
    if not np.isclose(np.sum(x_p), 1.0, rtol=0.0, atol=1e-6):
        raise ValueError("Probabilities do not sum to 1")
    
    x_a = np.array(x)
    
    return x_a @ x_p
    # pass
