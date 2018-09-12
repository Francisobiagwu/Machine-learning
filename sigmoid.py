def sigmoid(z):
    """used to compute the sigmoid function"""
    import numpy as np
    s = 1/(1+np.exp(-z))
    ### END CODE HERE ###
    
    return s
